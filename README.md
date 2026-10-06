# Python guardrails template

A [Copier](https://copier.readthedocs.io/) template for Python projects whose architecture and
quality rules are enforced by checks rather than by review. It is meant for code written with AI
coding agents: the agent can move fast because every rule it might bend fails `make verify`.

## What a generated project gets

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

## Use

Requires Docker and [Copier](https://copier.readthedocs.io/en/stable/#installation).

```sh
copier copy gh:sg4tech/python-guardrails-template my-project
cd my-project
git init && git add --all && git commit -m "Start from the guardrails template"
make install-hooks
make verify
```

Pull later improvements of the template into the project:

```sh
copier update
```

Copier merges the template's changes with yours and marks conflicts like `git merge`.

## Developing the template

`make test-template` generates a project from the current commit and runs its `make verify`; CI
runs the same on every pull request.

## License

MIT
