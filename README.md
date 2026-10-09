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
[playbook](https://sg4.tech/blog/code-entropy-ci-checks-ai-legacy/playbook.md) instead:
*Apply https://sg4.tech/blog/code-entropy-ci-checks-ai-legacy/playbook.md to this repository.*

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

- **Layers** `bootstrap → presentation | adapters → application → domain`, held by import-linter
  contracts; every application slice is listed, so a module dropped outside a slice fails.
- **Thin command-line handlers** (optional, on by default): each `handle_<command>(args, service,
  view)` calls one service method and hands its result to the view, with no branching, printing,
  construction or ambient state; a command-line module without handlers fails too.
- **Semgrep rules for what imports cannot express**: domain and application code imports only
  its own code and pure standard modules and does no direct I/O; the wall clock and the
  environment are read only where composition allows; value objects are frozen, domain services
  stateless, entities compared by identity; the composition root holds no logic; objects are not
  built by copying another's fields one by one.
- **Tests of the rules themselves**: every Semgrep rule is checked against fixtures it must and
  must not flag, so a rule that silently stops matching fails the build.
- **Quality gates**: ruff, strict mypy, pytest with branch coverage, bandit, deptry, pip-audit,
  vulture, cyclomatic and cognitive complexity, annotation complexity, pylint duplication and
  size limits, a package-size limit, and a mirrored test layout.
- **A commit-time secret scanner** with a pre-commit hook: tokens, keys, personal paths, local
  databases and log files.
- **Docker for every tool**, a `make verify` gate and a GitHub Actions workflow running it.
- **`AGENTS.md`** stating the rules for coding agents and people alike.
- **A small notes slice** that exercises every layer, so `make verify` passes right after
  generation; replace it with your own code.

## Developing the template

`make test-template` generates a project from the current commit and runs its `make verify`; CI
runs the same on every pull request.

## License

MIT
