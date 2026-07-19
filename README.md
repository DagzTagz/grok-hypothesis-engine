# DagzTagz Hypothesis Engine

**An open-source, community-driven system for generating, verifying, and testing scientific hypotheses.**  
**Powered by Grok (xAI)** — not an official xAI product.

The goal of this project is to create a transparent, auditable AI tool that helps researchers and curious minds propose novel scientific hypotheses, act as a peer adversary to rigorously check them against existing knowledge, and suggest practical ways to test them.

This project is inspired by xAI’s mission to advance our understanding of the universe through maximally truth-seeking AI. Live model calls use the **xAI Grok API** under **your** account and terms.

> **Current Status**: Early development (Phase 1). We are building a simple, working MVP.

---

## Vision

We want to build an AI system that acts like a thoughtful scientific collaborator:

- Proposes interesting, testable hypotheses grounded in real science
- Critically verifies those hypotheses for consistency and plausibility
- Suggests concrete experiments or simulations to personally test hypothesis against criticisms of hypothesis
- Maintains a clear, auditable record of its reasoning

The long-term vision is a multi-agent system that can assist with real scientific discovery while staying honest about what it knows and doesn’t know.

---

## Current Features (Phase 1 - MVP)

- Basic hypothesis generation from a topic or short description
- Structured output (hypothesis + verification + suggested tests)
- Simple verification step that checks for obvious contradictions
- Designed to be easy to run and understand

**Note**: This is still very early. The system is currently a single, well-prompted workflow rather than a full multi-agent system.

---

## How It Works (High Level)

1. You give the system a scientific topic or research area
2. It builds a short **background brief** (Phase 1: model knowledge only — not a live literature search)
3. It generates one or more hypotheses
4. It verifies each hypothesis for scientific consistency (thinking adversarially)
5. It suggests ways to test the hypothesis (experiments or code simulations)
6. Everything is output in a clear, structured format with reasoning (avoids black box reasoning)

---

## Getting Started

> ### Start with `--dry-run` (recommended for everyone)
>
> **Before** you add an API key or make live calls, install the project and run a **dry-run**.
> Dry-run uses **mock output only**: no xAI network request, no API key, no model charges.
>
> ```bash
> git clone https://github.com/DagzTagz/dagztagz-hypothesis-engine.git
> cd dagztagz-hypothesis-engine
> python3 -m venv .venv
> source .venv/bin/activate   # Windows: .venv\Scripts\activate
> pip install -e ".[dev]"
> hypothesis-engine --dry-run "photosynthesis under low light"
> ```
>
> You should see labeled mock hypotheses and: *“Dry-run mock output; no API calls were made.”*  
> Full walkthrough: **[getting-started.md](getting-started.md)**.

### Why dry-run first?

| Dry-run (`--dry-run`) | Live run (no flag) |
|----------------------|--------------------|
| No `XAI_API_KEY` needed | Requires your xAI key |
| No call to `api.x.ai` | Sends prompts + topic to xAI (Grok) |
| **$0 — no model charges** | **Bills your xAI account (real money/credits)** |
| Safe way to verify install | Real Grok generations (powered by xAI) |
| Mock text only | Model-generated science aid |

### Disclosures (please read)

- **Not malware, but not magic:** this repo is ordinary open-source Python. Clone and `pip install` do **not** by themselves call xAI. Live mode **does** use the network when **you** run it without `--dry-run`.
- **Your API key is your secret:** put it in a local `.env` (see `.env.example`). **Never commit** `.env` or paste keys into issues, PRs, or the topic string.
- **Live mode leaves your machine:** topic text and prompts are sent to **xAI** under **your** account/terms (including xAI’s terms and Acceptable Use Policy). Do not put passwords, private data, or keys in the topic.
- **Not established science:** outputs are experimental research aids. Always verify with experts and real methods.
- **Not an official xAI product:** **DagzTagz Hypothesis Engine** is a community project. **Powered by Grok (xAI)** means we call the public Grok API — it does **not** mean endorsement, partnership, or sponsorship by xAI. See [Disclaimer](#disclaimer) and [SECURITY.md](SECURITY.md).

---

### ⚠️ COST WARNING — LIVE MODE SPENDS REAL MONEY

> ## LIVE MODE IS NOT FREE
>
> Running **without** `--dry-run` calls the **xAI paid API** (Grok) with **your** `XAI_API_KEY`.
>
> - **You** pay for tokens / credits on **your** xAI account ([console.x.ai](https://console.x.ai) / xAI pricing).
> - This project does **not** pay for your usage and cannot cap your bill for you.
> - Phase 1 makes **multiple** model calls per run (background + generate + verify each hypothesis + tests). Costs scale with `-n` / `--num-hypotheses` and topic length.
> - Repeating live runs, automation, or large `-n` values can **add up quickly**.
> - **Dry-run costs $0.** Use it until you deliberately accept live charges.
>
> **Only use live mode if you understand and accept API billing on your account.**
> Check your xAI balance/limits before running live. This community project is **not responsible** for unexpected API charges.

---

### Live mode (only after dry-run works — **costs money**)

```bash
cp .env.example .env
# edit .env → set XAI_API_KEY=...

# WARNING: this line bills your xAI account — omit --dry-run on purpose
hypothesis-engine "effects of microplastics on soil microbiomes" -n 2
```

Live runs are **powered by Grok (xAI)**. Output is attributed accordingly; still not an official xAI product.

### Option 2: Using Grok Build (for faster development)

Since Grok Build (xAI’s open-source coding agent) is available, contributors may use it to help build and extend **DagzTagz Hypothesis Engine**. Still prefer **`--dry-run` first** when checking a local checkout.

---

## Development & Attribution

This project is being developed as an **open community effort** under the **DagzTagz** brand.

**Powered by Grok (xAI):**
- Live inference uses the **xAI Grok API** (OpenAI-compatible endpoint). You need your own `XAI_API_KEY` and must follow xAI’s terms.
- We attribute model-backed results to Grok/xAI as the **API provider**, not as the product owner.

**Pair programming with Grok:**
- Much of the initial architecture, prompt design, code scaffolding, and iterative development has been done through close collaboration with **Grok**, an AI built by xAI.
- Grok has served as a pair programmer — helping with ideas, code, explanations, and problem-solving.
- All final code, design decisions, and responsibility for the project belong to the human contributors (**DagzTagz** and community).

We believe in being transparent about AI assistance.

Special thanks to **xAI** for open-sourcing models/tools and offering an API that community projects can build on.

---

## Contributing

We warmly welcome contributors of all backgrounds and skill levels.

You don’t need to be a professional programmer to help. Contributions can include:
- Testing the current version and giving feedback
- Improving prompts and verification logic
- Adding better documentation
- Suggesting new features
- Helping with scientific domain knowledge
- Writing examples and test cases

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Even if you just want to follow along or ask questions, feel free to open an issue.

---

## Roadmap

### Phase 1 (Current)
- Simple working MVP (single workflow)
- Basic hypothesis generation + verification
- Clear structured output

### Phase 2
- Add literature retrieval (RAG)
- Improve verification with multiple checks
- Add experiment suggestion capabilities

### Phase 3
- Multi-agent architecture (Generator + Verifier + Experiment Designer)
- Better audit logging and transparency
- Web interface

### Long-term
- Domain-specific modes (Physics, Biology, Materials Science, etc.)
- Integration with real scientific tools and simulators
- Community-curated knowledge base

---

## License

This project is licensed under the **Apache License 2.0**.

You are free to use, modify, and distribute this software under that license.

---

## Acknowledgments

- **DagzTagz** community and contributors
- **xAI / Grok** — API and pair-programming assistance (**powered by Grok (xAI)**; not an official product)
- The broader open-source AI and scientific community (especially projects like Open Coscientist and related research on AI hypothesis generation)

---

## Disclaimer

**DagzTagz Hypothesis Engine** is a community project and is **not** an official product of xAI.  
It is **powered by Grok (xAI)** when used in live mode: that means the project calls the Grok API; it does **not** mean xAI endorses, sponsors, or operates this software.

It is an experimental tool meant to assist scientific thinking. Always verify any hypotheses or suggestions with real experts and proper scientific methods.

**Safety defaults:** prefer `hypothesis-engine --dry-run "…"` until you intentionally enable live API use. Dry-run does not contact xAI and costs **$0**. **Live mode bills your xAI account** (real money/credits); see [COST WARNING](#️-cost-warning--live-mode-spends-real-money).

---

**Let’s build something useful together.**

If you’re interested in contributing, have feedback, or just want to follow the project, feel free to star the repo, open an issue, or reach out.
