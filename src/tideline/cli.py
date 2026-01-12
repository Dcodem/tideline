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
