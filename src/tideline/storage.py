from pathlib import Path
from datetime import datetime

from .config import log_path
LOG = log_path()

def add_entry(text: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')}\t{text}\n")


def recent(limit: int = 20):
    if not LOG.exists():
        return []
    return LOG.read_text().splitlines()[-limit:]

# mkdir is idempotent
