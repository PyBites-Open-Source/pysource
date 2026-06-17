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

```
$ pysource -m re.match
def match(pattern, string, flags=0):
	"""Try to apply the pattern at the start of the string, returning
	a Match object, or None if no match was found."""
	return _compile(pattern, flags).match(string)
```

It also resolves C-implemented stdlib objects by falling back to their pure-Python source:

```
$ pysource -m datetime.date
class date:
    """Concrete date type.
    ...
```

To show the resulting code with paging add `-p` to the `pysource` command, so in this case: `pysource -m re.match -p`.

Check out [our blog post](https://pybit.es/get-python-source.html) for a demo.

### Vim integration

If you want to dump `pysource`'s output to a vertical split window I recommend installing [`ConqueTerm`](https://github.com/gingerhot/conque-term-vim) and then add this to your `.vimrc`:

```
nmap <leader>s :ConqueTermVSplit pysource -m <C-R><C-A><CR>
```

Now if you hit `<leader>s` (`,s` in my case as my Vim _leader_ key is `,`) on any object, it will open a split window with the source code (if it can be found, otherwise you will see a `ModuleNotFoundError`).

## Development

This project uses [uv](https://docs.astral.sh/uv/). To set up and run the tests:

	$ uv sync
	$ uv run pytest

Linting, formatting, and type checking run via [prek](https://github.com/j178/prek):

	$ uv run prek run --all-files

---

Enjoy!
