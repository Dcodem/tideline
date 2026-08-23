from click.testing import CliRunner

from tideline.cli import main


def test_help():
    r = CliRunner().invoke(main, ['--help'])
    assert r.exit_code == 0
