"""Command-line interface for the Phase 1 MVP."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from hypothesis_engine import __version__
from hypothesis_engine.workflow import bundle_to_json, run_workflow


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hypothesis-engine",
        description=(
            "DagzTagz Hypothesis Engine — generate, adversarially verify, "
            "and suggest tests for scientific hypotheses (Phase 1). "
            "Powered by Grok (xAI) in live mode."
        ),
    )
    parser.add_argument(
        "topic",
        nargs="?",
        help="Scientific topic or short description (or pass via --topic)",
    )
    parser.add_argument("--topic", dest="topic_opt", help="Alternative to positional topic")
    parser.add_argument(
        "-n",
        "--num-hypotheses",
        type=int,
        default=2,
        help="Number of hypotheses to generate (1-5, default: 2)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not call the API; emit deterministic mock structured output",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Write full JSON result to this file",
    )
    parser.add_argument(
        "--json-only",
        action="store_true",
        help="Print only JSON to stdout (no rich tables)",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    topic = (args.topic_opt or args.topic or "").strip()
    if not topic:
        parser.error("topic is required (positional or --topic)")

    console = Console(stderr=False)
    try:
        bundle = run_workflow(
            topic,
            n_hypotheses=args.num_hypotheses,
            dry_run=args.dry_run,
        )
    except Exception as exc:  # noqa: BLE001 — CLI boundary
        Console(stderr=True).print(f"[red]Error:[/red] {exc}")
        return 1

    payload = bundle_to_json(bundle)
    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")

    if args.json_only:
        print(payload)
        return 0

    _print_human(console, bundle)
    if args.output:
        console.print(f"\n[dim]Wrote JSON to {args.output}[/dim]")
    return 0


def _print_human(console: Console, bundle: object) -> None:
    # Late import-friendly typing: bundle is HypothesisBundle
    from hypothesis_engine.models import HypothesisBundle

    assert isinstance(bundle, HypothesisBundle)
    console.print(
        Panel.fit(
            f"[bold]{bundle.topic}[/bold]\n[dim]{bundle.overall_notes}[/dim]",
            title="DagzTagz Hypothesis Engine (Phase 1)",
        )
    )
    console.print("\n[bold]Background[/bold]")
    console.print(bundle.background.summary)
    if bundle.background.known_limitations:
        console.print("[dim]Limitations: " + "; ".join(bundle.background.known_limitations) + "[/dim]")

    for hyp in bundle.hypotheses:
        console.print(f"\n[bold cyan]{hyp.id}[/bold cyan]  {hyp.statement}")
        console.print(f"  [dim]Rationale:[/dim] {hyp.rationale}")
        ver = next((v for v in bundle.verifications if v.hypothesis_id == hyp.id), None)
        if ver:
            console.print(
                f"  [bold]Verdict:[/bold] {ver.verdict.value} "
                f"({ver.confidence.value}) — {ver.consistency_notes}"
            )
        tests = [t for t in bundle.tests if t.hypothesis_id == hyp.id]
        if tests:
            table = Table(title=f"Tests for {hyp.id}", show_lines=False)
            table.add_column("Title")
            table.add_column("Method")
            table.add_column("Falsify if…")
            for t in tests:
                table.add_row(t.title, t.method, t.what_would_falsify)
            console.print(table)

    powered = ""
    if not bundle.meta.get("dry_run"):
        powered = " Powered by Grok (xAI)."
    console.print(
        "\n[dim]DagzTagz Hypothesis Engine — experimental research aid; "
        f"not established science. Not an official xAI product.{powered}[/dim]"
    )


if __name__ == "__main__":
    sys.exit(main())
