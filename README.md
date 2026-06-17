# PyBites Pysource

A command line tool to read Python source code.

_Update 5th of Nov 2021_: we did not know it at the time, but this actually can be accomplished by Python's `inspect` module! So you might want to use that over this tool, for more info see [this Twitter thread](https://twitter.com/bbelderbos/status/1456234396810362885).


## Installation

Run it without installing anything using [uv](https://docs.astral.sh/uv/):

    uvx --from pybites-pysource pysource -m datetime.date

To make that an alias, add to your shell config:

    alias pysource='uvx --from pybites-pysource pysource'

Or install it from [PyPI](https://pypi.org/project/pybites-pysource/):

    uv tool install pybites-pysource

This tool requires Python 3.12+.

## Usage

Pass any importable object as `module(.submodule).name` with `-m`.

**A function:**

```
$ pysource -m re.match
def match(pattern, string, flags=0):
    """Try to apply the pattern at the start of the string, returning
    a Match object, or None if no match was found."""
    return _compile(pattern, flags).match(string)
```

**A class:**

```
$ pysource -m argparse.ArgumentParser
class ArgumentParser(_AttributeHolder, _ActionsContainer):
    """Object for parsing command line strings into Python objects.
    ...
```

**A whole module** (omit the trailing name):

```
$ pysource -m string
"""A collection of string constants.
...
```

**A C-implemented stdlib object** — `pysource` falls back to the pure-Python source (`datetime`, `decimal`, `io`):

```
$ pysource -m decimal.Decimal
class Decimal(object):
    """Floating-point class for decimal arithmetic."""
    ...
```

**No source available** — when an object is implemented in C with no Python equivalent, you get a clear message (and a non-zero exit code) instead of a traceback:

```
$ pysource -m builtins.len
no Python source available for 'len' (likely implemented in C / a builtin)
```

**Paging** — add `-p` (or `--pager`) to page long output, e.g. `pysource -m argparse.ArgumentParser -p`.

Check out [our blog post](https://pybit.es/get-python-source.html) for a demo.

### Pipe into your editor

Since `pysource` writes to stdout, you can pipe it straight into Vim (the `-` reads from stdin):

```
$ pysource -m re.match | vim -
```

Add `-c 'set ft=python'` for syntax highlighting: `pysource -m re.match | vim - -c 'set ft=python'`.

### Vim integration

If you use [jedi-vim](https://github.com/davidhalter/jedi-vim), you already have source navigation built in — just hit `,s` on an object to jump to its definition, no extra mapping needed.

## Development

This project uses [uv](https://docs.astral.sh/uv/). To set up and run the tests:

	$ uv sync
	$ uv run pytest

Linting, formatting, and type checking run via [prek](https://github.com/j178/prek):

	$ uv run prek run --all-files

---

Enjoy!
