import json

from . import storage


def to_json() -> str:
    items = []
    for line in storage.recent(10_000):
        ts, _, text = line.partition("\t")
        items.append({"ts": ts, "text": text.rstrip()})
    return json.dumps(items, indent=2)

# entries without a tab still export with empty text
