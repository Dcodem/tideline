import os
from pathlib import Path


def log_path() -> Path:
    override = os.environ.get("TIDELINE_LOG")
    if override:
        return Path(override).expanduser()
    return Path.home() / ".tideline" / "log.txt"

# resolved at import time
