# Python guardrails template

AI coding agents write code fast and pile up legacy just as fast. This template starts a Python
project with checks that fail the build when that happens, so the agent has to fix the code
instead.

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

Requires Docker and [Copier](https://copier.readthedocs.io/en/stable/#installation).

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

What a generated project gets:

- **One gate:** `make verify` runs every check in Docker; GitHub Actions runs the same.
- **Checks:** ruff, strict mypy, pytest with branch coverage, complexity and size limits,
  copy-paste, dead code, dependency and vulnerability audit, bandit.
- **Architecture:** business logic is kept apart from the database, network and CLI, and can't
  import them. Enforced by import-linter and Semgrep:
  - domain and application code do no I/O
  - value objects are frozen, services are stateless
  - only `bootstrap/` builds objects
  - the rules are tested, so a rule that stops working fails the build
- **Thin CLI handlers** (optional): one service call per command.
- **Secret scanner** on every commit.
- **`AGENTS.md`** with the rules for agents and people.
- **A small example** that passes `make verify`; replace it with your code.

## Developing the template

`make test-template` generates a project from the current commit and runs its `make verify`; CI
runs the same on every pull request.

## License

MIT
