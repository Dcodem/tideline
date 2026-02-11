import click
from . import storage

@click.group()
def main():
    """tideline - a tiny daily log."""

@main.command()
@click.argument("text", nargs=-1)
def new(text):
    """Add a new entry."""
    storage.add_entry(" ".join(text))

if __name__ == "__main__":
    main()


@main.command("list")
@click.option("-n", "--limit", default=20, help="Number of entries.")
def list_(limit):
    """List recent entries."""
    for line in storage.recent(limit):
        click.echo(line.rstrip())

# entrypoint for `tideline` script


@main.command()
@click.argument("query")
def find(query):
    """Search entries."""
    from .search import find as _find
    for line in _find(query):
        click.echo(line.rstrip())


@main.command()
def export():
    """Export entries as JSON."""
    from .export import to_json
    click.echo(to_json())


@main.command()
def edit():
    """Open the log file in $EDITOR."""
    import os, subprocess
    from .config import log_path
    subprocess.call([os.environ.get("EDITOR", "vi"), str(log_path())])
