"""Offline workflow tests using --dry-run style mock path."""

import json

import pytest

from hypothesis_engine.cli import main
from hypothesis_engine.llm import parse_json_object
from hypothesis_engine.workflow import run_workflow


def test_dry_run_bundle_shape():
    bundle = run_workflow("quantum biology", n_hypotheses=2, dry_run=True)
    assert bundle.topic == "quantum biology"
    assert len(bundle.hypotheses) == 2
    assert len(bundle.verifications) == 2
    assert bundle.meta.get("dry_run") is True
    payload = json.loads(bundle.model_dump_json())
    assert "background" in payload


def test_empty_topic_raises():
    with pytest.raises(ValueError):
        run_workflow("  ", dry_run=True)


def test_parse_json_with_fences():
    text = """Here you go:\n```json\n{\"a\": 1}\n```\n"""
    assert parse_json_object(text) == {"a": 1}


def test_cli_dry_run_json(capsys):
    code = main(["--dry-run", "--json-only", "test topic", "-n", "1"])
    assert code == 0
    out = capsys.readouterr().out
    data = json.loads(out)
    assert data["topic"] == "test topic"
    assert len(data["hypotheses"]) == 1
