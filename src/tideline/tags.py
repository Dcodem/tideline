import re

TAG_RE = re.compile(r"#([a-zA-Z0-9_-]+)")

def extract(text: str) -> list[str]:
    return TAG_RE.findall(text)
