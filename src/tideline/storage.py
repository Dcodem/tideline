from pathlib import Path
from datetime import datetime

from .config import log_path
LOG = log_path()

def add_entry(text: str) -> None:
    if not text.strip():
        return
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')}\t{text}\n")


def recent(limit: int = 20):
    if not LOG.exists() or not LOG.stat().st_size:
        return []
    return LOG.read_text().splitlines()[-limit:]

# mkdir is idempotent


def pop_last() -> str | None:
    if not LOG.exists():
        return None
    lines = LOG.read_text().splitlines()
    if not lines:
        return None
    last = lines[-1]
    LOG.write_text("\n".join(lines[:-1]) + ("\n" if lines[:-1] else ""))
    return last

# guard against double newlines


# TODO: tail-read for very large logs
