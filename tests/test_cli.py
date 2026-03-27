

def test_find_runs():
    from click.testing import CliRunner
    from tideline.cli import main
    r = CliRunner().invoke(main, ['find', 'xyz'])
    assert r.exit_code == 0
