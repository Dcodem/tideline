from collections import Counter
from . import storage, tags

def tag_counts() -> Counter:
    c = Counter()
    for line in storage.recent(100_000):
        c.update(tags.extract(line))
    return c

# single source of truth for log iteration
