# tideline

A tiny CLI for keeping a daily log. One file, one line per entry. Simple as that.

## Install

```
pip install -e .
```

## Usage

```
tideline new "wrapped up the q2 plan"
tideline list -n 10
```


Or install from PyPI once published.

Weekly review: `tideline find '#review' && tideline stats`.

## Roadmap

- sqlite backend (optional)
- richer search
- markdown export

`tideline edit` opens the raw log in your $EDITOR.

Simple, really.

<!-- coverage badge TBD -->

`tideline stats` prints the most-used tags.

Not safe for concurrent writes from multiple processes.

Export is a JSON array of `{ts, text}` objects.

Set `TIDELINE_LOG` to point at a different file.
