from tideline import storage

def test_add_and_recent(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "LOG", tmp_path / "log.txt")
    storage.add_entry("hello")
    storage.add_entry("world")
    out = storage.recent(10)
    assert len(out) == 2
    assert "hello" in out[0]
    assert "world" in out[1]


from tideline.tags import extract

def test_extract_tags():
    assert extract('hello #work #q2-plan') == ['work', 'q2-plan']


def test_blank_ignored(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, 'LOG', tmp_path / 'l.txt')
    storage.add_entry('   ')
    assert storage.recent() == []
