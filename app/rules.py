import re

RULES = [
    {"name": "SQL Injection", "pattern": re.compile(r"(?i)(union|select|or\s+1=1|--)")},
    {"name": "XSS", "pattern": re.compile(r"<script.*?>.*?</script>", re.IGNORECASE)},
    {"name": "LFI", "pattern": re.compile(r"(\.\./)+")},
    {"name": "RCE", "pattern": re.compile(r"(;|\|\||&&)\s*(\w+)")},
]
