from tideline import storage

def test_add_and_recent(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "LOG", tmp_path / "log.txt")
    storage.add_entry("hello")
    storage.add_entry("world")
    out = storage.recent(10)
    assert len(out) == 2
    assert "hello" in out[0]
    assert "world" in out[1]
