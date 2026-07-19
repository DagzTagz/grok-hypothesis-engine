"""Thin wrapper around the xAI (Grok) OpenAI-compatible API."""

from __future__ import annotations

import json
import re
from typing import Any

from openai import OpenAI

from hypothesis_engine.config import Settings


class LLMError(RuntimeError):
    """Raised when the model response cannot be used."""


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
) -> dict[str, Any]:
    """Call chat completions and parse a JSON object from the reply."""
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    content = response.choices[0].message.content
    if not content:
        raise LLMError("Empty model response")
    return parse_json_object(content)


def parse_json_object(text: str) -> dict[str, Any]:
    """Extract a JSON object from model text (allows optional markdown fences)."""
    cleaned = text.strip()
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", cleaned)
    if fence:
        cleaned = fence.group(1).strip()
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError:
        start = cleaned.find("{")
        end = cleaned.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise LLMError(f"Could not parse JSON from model output:\n{text[:500]}") from None
        data = json.loads(cleaned[start : end + 1])
    if not isinstance(data, dict):
        raise LLMError("Model JSON root must be an object")
    return data
