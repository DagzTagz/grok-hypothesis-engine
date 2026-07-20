"""Thin wrapper around the xAI (Grok) OpenAI-compatible API."""

from __future__ import annotations

import json
import re
from typing import Any

from openai import OpenAI

from hypothesis_engine.config import Settings


class LLMError(RuntimeError):
    """Raised when the model response cannot be used."""


# JSON allows \" \\ \/ \b \f \n \r \t \uXXXX — models often emit bare \path or \s etc.
_INVALID_JSON_ESCAPE = re.compile(r'\\(?!["\\/bfnrtu])')


def build_client(settings: Settings) -> OpenAI:
    api_key = settings.require_api_key()
    return OpenAI(api_key=api_key, base_url=settings.xai_base_url)


def chat_json(
    client: OpenAI,
    *,
    model: str,
    system: str,
    user: str,
    temperature: float = 0.4,
    max_parse_retries: int = 1,
) -> dict[str, Any]:
    """Call chat completions and parse a JSON object from the reply.

    Retries the model once if the first reply is not parseable JSON (common with
    invalid backslash escapes in long free-text fields).
    """
    last_error: Exception | None = None
    for attempt in range(max_parse_retries + 1):
        attempt_user = user
        if attempt > 0:
            attempt_user = (
                user
                + "\n\nIMPORTANT: Your previous reply was not valid JSON. "
                "Reply again with ONLY a single JSON object. "
                "In strings, escape backslashes as \\\\ and quotes as \\\". "
                "Do not use raw LaTeX or Windows-style paths without escaping."
            )
        response = client.chat.completions.create(
            model=model,
            temperature=temperature if attempt == 0 else min(temperature, 0.2),
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": attempt_user},
            ],
        )
        content = response.choices[0].message.content
        if not content:
            last_error = LLMError("Empty model response")
            continue
        try:
            return parse_json_object(content)
        except LLMError as exc:
            last_error = exc
            continue
    assert last_error is not None
    raise last_error


def parse_json_object(text: str) -> dict[str, Any]:
    """Extract a JSON object from model text (allows fences + light repair)."""
    cleaned = _strip_fences(text.strip())
    candidates = [cleaned]
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start != -1 and end > start:
        sliced = cleaned[start : end + 1]
        if sliced != cleaned:
            candidates.append(sliced)

    errors: list[str] = []
    for raw in candidates:
        for variant in (raw, _repair_json_text(raw)):
            try:
                data = json.loads(variant)
            except json.JSONDecodeError as exc:
                errors.append(str(exc))
                continue
            if not isinstance(data, dict):
                raise LLMError("Model JSON root must be an object")
            return data

    detail = errors[-1] if errors else "unknown parse error"
    raise LLMError(
        "Could not parse JSON from the model (often invalid \\ escapes in text). "
        f"Parser said: {detail}. Try the same command again."
    )


def _strip_fences(text: str) -> str:
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if fence:
        return fence.group(1).strip()
    return text


def _repair_json_text(s: str) -> str:
    """Best-effort fixes for common LLM JSON mistakes."""
    # Turn invalid \x sequences into \\x so json.loads accepts them as backslash + char
    s = _INVALID_JSON_ESCAPE.sub(r"\\\\", s)
    # Trailing commas
    s = re.sub(r",\s*}", "}", s)
    s = re.sub(r",\s*]", "]", s)
    return s
