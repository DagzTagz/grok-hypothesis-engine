# Contributing to Grok Hypothesis Engine

Thank you for your interest in contributing. This project is an **open community effort** to build a transparent, auditable tool for generating, verifying, and testing scientific hypotheses.

You do **not** need to be a professional programmer to help. Careful thinking, clear writing, scientific judgment, and good bug reports all count.

This is a community project and is **not** an official product of xAI.

---

## Before you start

1. Read the [README](README.md) for vision, Phase 1 scope, and roadmap.  
2. Skim [SECURITY.md](SECURITY.md) so you know how to handle secrets and vulnerability reports.  
3. Check [open issues](https://github.com/DagzTagz/grok-hypothesis-engine/issues) for something that matches your interest.  
4. For **large** changes (new architecture, new major feature, changing license or scope), open an issue first and wait for maintainer feedback before a big PR.

Small fixes (typos, docs clarity, obvious bugs) can go straight to a pull request.

---

## Ways to contribute

| Kind of help | Examples |
|--------------|----------|
| **Feedback & testing** | Try the MVP when it lands; report what was confusing or wrong |
| **Documentation** | README, getting-started, examples, clearer explanations |
| **Prompts & verification** | Better hypothesis prompts; stronger adversarial checks |
| **Code** | Scripts, structure, tests, tooling, small refactors |
| **Science** | Domain knowledge, example topics, sanity-check outputs |
| **Examples & fixtures** | Sample inputs/outputs for regression tests |
| **Issues** | Well-written bug reports and feature ideas |

If you are unsure where you fit, open an issue with the label idea “question” and say what you enjoy doing.

---

## Ground rules

- Be respectful and constructive. Assume good intent.  
- Prefer **truth-seeking** over hype: say what is uncertain; do not overclaim scientific results.  
- Keep Phase 1 **simple**. Prefer a clear MVP over premature multi-agent complexity.  
- **Never commit secrets** (API keys, tokens, private keys, recovery codes, real `.env` values). Use placeholders in examples.  
- Security issues → **private** report via [SECURITY.md](SECURITY.md), not a public issue.  
- Do not submit generated “walls of code” with no explanation of intent and tradeoffs.  
- This project welcomes AI-assisted work (including Grok Build) when humans remain responsible for review and decisions (see below).

---

## Development setup (Phase 1)

The MVP is still early. When runnable code exists, setup steps will live in `getting-started.md`. Until then:

```bash
git clone https://github.com/DagzTagz/grok-hypothesis-engine.git
cd grok-hypothesis-engine
```

- Work on a **branch**, not directly on `main`, if you have write access. Most people use a **fork + PR**.  
- Keep your branch up to date with `main` before opening or updating a PR.  
- Do not commit local junk (venv, `node_modules`, editor files). `.gitignore` already covers common cases.

---

## Pull request process

### 1. Fork and branch

```bash
# after forking on GitHub and cloning your fork
git checkout -b docs/fix-typo   # or fix/..., feat/..., etc.
```

Branch name tips: short and descriptive (`docs/security-link`, `fix/readme-typo`, `feat/hypothesis-schema`).

### 2. Make focused changes

- One PR ≈ one concern.  
- Match existing style when code exists.  
- Update docs if your change affects how people use the project.  
- Add or adjust tests when we have a test suite and your change is testable.

### 3. Commit messages

Use clear, present-tense summaries:

```text
docs: clarify adversarial verification in README
fix: handle empty topic input in generator
feat: add structured hypothesis JSON schema
```

Optional but appreciated: **signed commits** (`git commit -S`) if you use GPG/SSH signing. Not required for first-time contributors.

### 4. Open the pull request

- Fill in the PR description: **what** changed, **why**, and how to **test** it.  
- Link related issues (`Fixes #12` or `Related to #12`).  
- If AI tools helped, say so briefly (see **AI-assisted contributions**).  
- Be ready for review comments; iteration is normal.

### 5. Review and merge

Maintainers may ask for changes, split a PR, or decline work that fights the Phase 1 scope. That is about project direction, not a personal judgment.

---

## Issues: bugs and ideas

### Bug reports

Please include:

1. What you did  
2. What you expected  
3. What actually happened  
4. Environment (OS, Python/Node/Rust version if relevant, commit hash if known)  
5. Logs or screenshots **with secrets redacted**

### Feature requests

Describe the problem first, then a possible solution. Note whether it fits **Phase 1** or is better as later roadmap work.

### Security

Do **not** file public issues for vulnerabilities. Use [SECURITY.md](SECURITY.md).

---

## AI-assisted contributions

This project is built with transparent human–AI collaboration (including pair programming with **Grok** / Grok Build).

You may use AI tools to help write code, docs, or tests **if**:

1. **You understand** the change well enough to explain and defend it.  
2. **You review** every line for correctness, license, and secrets.  
3. **You remain responsible** for the contribution — tools do not own the commit.  
4. For non-trivial PRs, **mention AI assistance** in the PR description (which tools, roughly what they did).  
5. Do not paste **private keys, tokens, or personal data** into third-party AI tools.

Maintainers may request more human explanation on large AI-generated diffs.

---

## Code of conduct (summary)

We expect participants to:

- Be kind; no harassment, hate, or personal attacks  
- Stay on topic and avoid spam  
- Respect maintainers’ time and decisions about scope  
- Credit others’ work; no plagiarism  

Serious or repeated violations may result in warnings or being blocked from the project spaces. A fuller Code of Conduct document may be added later; until then, this summary applies.

---

## License

By contributing, you agree that your contributions are licensed under the same **Apache License 2.0** as this repository (see [LICENSE](LICENSE)).

You also confirm that you have the right to submit the work (it is yours, or you are allowed to contribute it under Apache-2.0).

---

## Attribution and credit

- Human contributors own project decisions and merged work.  
- Significant contributions may be acknowledged in release notes or an AUTHORS/CONTRIBUTORS list as the project grows.  
- Please do not imply official endorsement by xAI.

---

## Questions

- Product / design / “where should I start?” → open a GitHub **issue**  
- Security → [SECURITY.md](SECURITY.md) only  
- Quick clarification on an open PR → comment on that PR  

Welcome aboard — we are glad you are here.
