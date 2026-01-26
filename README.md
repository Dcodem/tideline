# tideline

A small CLI for keeping a daily log. One file, one line per entry.

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
