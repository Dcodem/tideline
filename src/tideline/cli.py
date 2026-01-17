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
