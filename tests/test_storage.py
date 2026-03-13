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


def test_extract_preserves_order():
    from tideline.tags import extract
    assert extract('#b #a') == ['b','a']


def test_pop_last(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, 'LOG', tmp_path / 'l.txt')
    storage.add_entry('one')
    storage.add_entry('two')
    assert 'two' in storage.pop_last()
    assert len(storage.recent()) == 1


def test_export_smoke(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, 'LOG', tmp_path / 'l.txt')
    storage.add_entry('a')
    from tideline.export import to_json
    import json
    assert json.loads(to_json())
