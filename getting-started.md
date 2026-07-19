# Getting Started — DagzTagz Hypothesis Engine (Phase 1 MVP)

This guide runs the **DagzTagz Hypothesis Engine** Phase 1 CLI: a single workflow that
proposes hypotheses, checks them adversarially, and suggests tests.

**Powered by Grok (xAI)** in live mode. **Not** an official xAI product.

## Requirements

- Python **3.11+**
- An [xAI API key](https://console.x.ai) for live runs (`XAI_API_KEY`)
- Git (to clone the repo)

Live calls use the **xAI OpenAI-compatible API** (`https://api.x.ai/v1`) with model
`grok-4.5` by default (**powered by Grok (xAI)**).

## Install (editable)

### 1. Get the code

Clone with Git (recommended — easy to update later with `git pull`):

```bash
git clone https://github.com/DagzTagz/dagztagz-hypothesis-engine.git
cd dagztagz-hypothesis-engine
```

If the GitHub repo was recently renamed, the old URL may redirect; prefer the name above.

If you downloaded a **ZIP** from GitHub instead: unzip it, then `cd` into the unzipped folder
(it may be named `dagztagz-hypothesis-engine-main` or similar).

### 2. Create a virtual environment and install

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

If `hypothesis-engine` is not found after install, confirm the venv is active and re-run `pip install -e ".[dev]"`. The command name is **`hypothesis-engine`** (not `hypothesis`).

## Configure secrets

```bash
cp .env.example .env
# edit .env and set XAI_API_KEY=...
```

Never commit `.env`. It is gitignored.

You can also:

```bash
export XAI_API_KEY=your_key_here
```

Prefer `.env` so the key is less likely to end up in shell history.

## Run (offline dry-run — no API key, $0 cost)

Useful to verify install and output shape:

```bash
hypothesis-engine --dry-run "photosynthesis under low light"
# or
python -m hypothesis_engine --dry-run "photosynthesis under low light"
```

JSON only:

```bash
hypothesis-engine --dry-run --json-only -n 1 "coral bleaching" -o out.json
```

## Run (live — powered by Grok (xAI), **costs money**)

```bash
hypothesis-engine "effects of microplastics on soil microbiomes" -n 2
```

**Warning:** live mode bills **your** xAI account (multiple API calls per run). Dry-run first.

Optional env overrides:

- `XAI_MODEL` (default `grok-4.5`)
- `XAI_BASE_URL` (default `https://api.x.ai/v1`)

Live users must follow [xAI’s terms](https://x.ai/legal/terms-of-service) and [Acceptable Use Policy](https://x.ai/legal/acceptable-use-policy).

## What the pipeline does

1. **Background brief** — model knowledge only (not RAG / not a paper search)
2. **Generate** N hypotheses (default 2)
3. **Verify** each adversarially (consistency, testability, contradictions)
4. **Suggest tests** with falsification criteria
5. Print a readable report and optional JSON

## Tests

```bash
pytest
```

## Security notes

- Keep keys out of the shell history when you can (prefer `.env`)
- See [SECURITY.md](SECURITY.md) for vulnerability reporting
- See [CONTRIBUTING.md](CONTRIBUTING.md) for PR workflow

## Disclaimer

**DagzTagz Hypothesis Engine** is an experimental research aid only. Not established science.  
**Powered by Grok (xAI)** when used live — **not** an official xAI product.
