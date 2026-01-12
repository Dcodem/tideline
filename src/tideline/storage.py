from pathlib import Path
from datetime import datetime

LOG = Path.home() / ".tideline" / "log.txt"

def add_entry(text: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')}\t{text}\n")
