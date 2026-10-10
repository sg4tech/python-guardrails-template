# Python guardrails template

[![Template](https://github.com/sg4tech/python-guardrails-template/actions/workflows/template.yml/badge.svg?branch=main)](https://github.com/sg4tech/python-guardrails-template/actions/workflows/template.yml)
[![License: MIT](https://img.shields.io/github/license/sg4tech/python-guardrails-template)](LICENSE)
[![Python 3.12 | 3.13](https://img.shields.io/badge/python-3.12%20%7C%203.13-blue)](copier.yml)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

**Guardrails for AI-generated Python code.**\
Instead of asking an agent to follow your conventions, make CI enforce them.

```sh
copier copy gh:sg4tech/python-guardrails-template my-project
```

**What fails the build:**

- unused code
- style and type errors
- untested changes
- functions that get too complex
- copy-paste
- imports that break the architecture
- leaked secrets

**Existing project, or not Python?** Give your coding agent the
[playbook](https://sg4.tech/blog/code-entropy-ci-checks-ai-legacy/playbook.md) with this prompt:

```text
Apply https://sg4.tech/blog/code-entropy-ci-checks-ai-legacy/playbook.md to this repository.
```

**Why these checks:**
[Code entropy: how CI checks keep AI from piling up legacy](https://sg4.tech/blog/code-entropy-ci-checks-ai-legacy/)

## Use

Requires Docker and [Copier](https://copier.readthedocs.io/en/stable/#installation). A generated project is a regular Python
project: `pyproject.toml` at the root, dependencies managed by uv.

```sh
copier copy gh:sg4tech/python-guardrails-template my-project
cd my-project
git init && git add --all && git commit -m "Start from the guardrails template"
make install-hooks
make verify
```

After generation it's a normal repository; `copier update` is optional and only pulls template
improvements if you want them. Pull later improvements of the template into the project:

```sh
copier update
```

Copier merges the template's changes with yours and marks conflicts like `git merge`.

## Details

| Job | Tool |
|---|---|
| Package manager | [uv](https://github.com/astral-sh/uv) |
| Lint and format | [ruff](https://github.com/astral-sh/ruff) |
| Types | [mypy](https://github.com/python/mypy) (strict) |
| Tests and coverage | [pytest](https://github.com/pytest-dev/pytest), [coverage](https://github.com/coveragepy/coveragepy) with a threshold |
| Complexity | [xenon](https://github.com/rubik/xenon) (cyclomatic), [complexipy](https://github.com/rohaquinlop/complexipy) (cognitive) |
| Copy-paste | [pylint](https://github.com/pylint-dev/pylint) duplicate-code |
| Dead code | [vulture](https://github.com/jendrikseipp/vulture) |
| Dependency hygiene | [deptry](https://github.com/osprey-oss/deptry) |
| Vulnerabilities | [pip-audit](https://github.com/pypa/pip-audit) |
| Security lint | [bandit](https://github.com/PyCQA/bandit) |
| Architecture | [import-linter](https://github.com/seddonym/import-linter), [Semgrep](https://github.com/semgrep/semgrep) |
| Secrets | built-in commit-time scanner |

What a generated project gets:

- **One gate:** `make verify` runs every check in Docker; GitHub Actions runs the same.
- **Architecture (Clean / Hexagonal):** business logic is kept apart from the database, network and CLI, and can't
  import them. Enforced by import-linter and Semgrep:
  - domain and application code do no I/O
  - value objects are frozen, services are stateless
  - only `bootstrap/` builds objects
  - the rules are tested, so a rule that stops working fails the build
- **Thin CLI handlers** (optional): one service call per command.
- **`AGENTS.md`** with the rules for agents and people.
- **A small example** (notes) that goes through every layer, so `make verify` passes right after
  generation and an agent has a pattern to copy for new features. Start at `application/notes/`.

## Examples

Two shortcuts an agent takes, and what CI says:

Copying a function instead of reusing it:

```text
R0801: Similar lines in 2 files
==demo_notes.domain.services.note_preview:[1:6]
==demo_notes.domain.services.note_summary:[1:6]
    words = text.split()
    if len(words) <= 12:
        return " ".join(words)
    ...
```

Business logic importing the storage adapter directly:

```text
Layered architecture BROKEN
demo_notes.application is not allowed to import demo_notes.adapters:
- demo_notes.application.notes.add_note ->
  demo_notes.adapters.persistence.json_note_store (l.1)
```

Either one keeps the build red until the code is fixed.

## Developing the template

`make test-template` generates a project from the current commit and runs its `make verify`; CI
runs the same on every pull request.

## License

MIT
