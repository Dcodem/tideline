from . import storage

def find(query: str):
    q = query.lower()
    for line in storage.recent(10_000):
        if q in line.lower():
            yield line

# query is case-insensitive
