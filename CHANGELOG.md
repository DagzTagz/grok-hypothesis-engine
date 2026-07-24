# Changelog

All notable changes to **DagzTagz Hypothesis Engine** are documented here.

This project is **early, iterative open source** — not a finished product. We disclose privacy and security-relevant changes **up front** so people who already cloned, pip-installed, or downloaded a ZIP can **update and harden** their local copies.

The format is based on [Keep a Changelog](https://keepachangelog.com/).  
Versions follow [Semantic Versioning](https://semver.org/) while pre-1.0 (`0.x` = public iterations; expect breaking changes until 1.0).

---

## [0.2.0] — 2026-07-23 — second public iteration

**Think of this as “version 2” of the public project:** Phase 2 features plus a **local privacy fix** that matters if you still have files from older runs.

### Privacy fix (action needed if you ran older builds)

**Issue:** Before `0.2.0`, files created by `-o` / `--output` and `--audit-log` often used the default umask (commonly mode **`0644` or `0664`**). On multi-user machines that means **other local accounts** could read those files (“group/world-readable” in Unix terms — not “the whole internet,” but **any user on the same computer** who can open the path).

**What was in those files:**

| File | Typical content risk |
|------|----------------------|
| `-o out.json` | Full **plaintext** topic, hypotheses, multi-check, suggested tests |
| `--audit-log audit.jsonl` | Run metadata; topics hashed or encrypted by default, but still a local paper trail |

**What we fixed in code (0.2.0+):**

- New and rewritten `-o` outputs are created as mode **`0600`** (owner read/write only).
- `--audit-log` files are created as **`0600`**; each append **re-tightens** mode to `0600` (helps existing loose logs).

**What you should do if you used 0.1.x or an older ZIP/clone:**

```bash
cd /path/to/dagztagz-hypothesis-engine   # or wherever your files live

# 1) Pull / re-download / reinstall so you have 0.2.0+ code
git pull   # or download a fresh ZIP of main / the 0.2.0 release

# 2) Reinstall into your venv
source .venv/bin/activate
pip install -e ".[dev]"   # or pip install -e ".[audit]" as you prefer

# 3) Harden ANY existing local outputs you care about
chmod 600 .env out.json audit.jsonl 2>/dev/null || true
# add any other -o paths you used

# 4) Confirm
stat -c '%a %n' .env out.json audit.jsonl
# expect 600 for each file that exists
```

This is **local OS hygiene**, not encryption and not a cloud breach. Full-disk encryption and account lock still matter for stronger threats.

See also [SECURITY.md — Privacy notices for existing installs](SECURITY.md#privacy-notices-for-existing-installs) and [getting-started.md — File permissions](getting-started.md#file-permissions-owner-only).

### Added (Phase 2 product slices included in this iteration)

- **Multi-check verification** (`meta.verification = multi_check_v1`): consistency, testability, confounds, prior_knowledge.
- **Richer experiment suggestions** (`meta.tests = richer_tests_v1`): what is measured, controls, materials/data, addresses_checks, rough duration.

### Changed

- CLI writes private output/audit files as **`0600`**.
- Docs: README, getting-started, SECURITY privacy notice; package version **0.2.0**.

### Security / honesty notes

- Still **alpha research aid**, not established science, not an official xAI product.
- **Live mode** still sends topics to xAI under **your** key; file modes do not change that.
- Dry-run remains free and offline.

---

## [0.1.0] — 2026-07 — first public MVP iteration

- Phase 1 single workflow: background → generate → verify → suggest tests.
- Dry-run mocks, live xAI path with cost confirmation, optional audit log (hash / encrypt / plaintext opt-in).
- CI (pytest + ruff), Dependabot, SECURITY / CONTRIBUTING / getting-started.
- Default audit and `-o` file modes depended on umask (**often group/world-readable**) — **fixed in 0.2.0**.

---

## Links

- Repository: https://github.com/DagzTagz/dagztagz-hypothesis-engine  
- Security policy: [SECURITY.md](SECURITY.md)  
- ZIP of latest `main`: https://github.com/DagzTagz/dagztagz-hypothesis-engine/archive/refs/heads/main.zip  
