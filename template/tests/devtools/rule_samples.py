"""A small rule set the scanner tests read instead of the project's own configuration."""

SAMPLE_RULES = """
allow_marker = "secret-scan: allow"

[[content_rules]]
id = "api-key"
description = "API key"
pattern = "sk-[A-Za-z0-9_-]{20,}"

[[path_rules]]
id = "log-file"
description = "Log file"
pattern = "\\\\.log$"
"""
