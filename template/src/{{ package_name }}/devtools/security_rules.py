"""Pure rule model and matching for the commit-time secret scanner."""

import re
import tomllib
from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    identifier: str
    description: str
    pattern: re.Pattern[str]


@dataclass(frozen=True)
class RuleSet:
    allow_marker: str
    content_rules: tuple[Rule, ...]
    path_rules: tuple[Rule, ...]


@dataclass(frozen=True)
class Finding:
    """A rule hit; it names the rule and place but never echoes the matched text."""

    path: str
    line: int | None
    rule_id: str
    description: str


def parse_rules(text: str) -> RuleSet:
    document = tomllib.loads(text)
    return RuleSet(
        allow_marker=str(document["allow_marker"]),
        content_rules=_parse_rule_table(document.get("content_rules", [])),
        path_rules=_parse_rule_table(document.get("path_rules", [])),
    )


def _parse_rule_table(entries: list[dict[str, str]]) -> tuple[Rule, ...]:
    return tuple(
        Rule(entry["id"], entry["description"], re.compile(entry["pattern"])) for entry in entries
    )


def scan_path(rules: RuleSet, path: str) -> list[Finding]:
    return [
        Finding(path, None, rule.identifier, rule.description)
        for rule in rules.path_rules
        if rule.pattern.search(path)
    ]


def scan_text(rules: RuleSet, path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for number, line in enumerate(text.splitlines(), start=1):
        if rules.allow_marker in line:
            continue
        findings.extend(
            Finding(path, number, rule.identifier, rule.description)
            for rule in rules.content_rules
            if rule.pattern.search(line)
        )
    return findings
