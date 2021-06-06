# PyBites Pysource

A command line tool to read Python source code.

## Installation

You can install `pybites-pysource` from [PyPI](https://pypi.org/project/pybites-pysource/):

    pip install pybites-pysource

Or use `pipx` if you want to have it available globally.

This tool uses Python 3.x

## Usage

You can use `pybites-pysource`:

```
$ pysource -m re.match
def match(pattern, string, flags=0):
	"""Try to apply the pattern at the start of the string, returning
	a Match object, or None if no match was found."""
	return _compile(pattern, flags).match(string)
```

To show the resulting code with paging add `-p` to the `pysource` command, so in this case: `pysource -m re.match -p`.

Check out [our blog post](https://pybit.es/get-python-source.html) for a demo.

### Vim integration

If you want to dump `pysource`'s output to a vertical split window I recommend installing [`ConqueTerm`](https://github.com/gingerhot/conque-term-vim) and then add this to your `.vimrc`:

```
nmap <leader>s :ConqueTermVSplit pysource -m <C-R><C-A><CR>
```

Now if you hit `<leader>s` (`,s` in my case as my Vim _leader_ key is `,`) on any object, it will open a split window with the source code (if it can be found, otherwise you will see a `ModuleNotFoundError`).

## Tests

To run the tests:

	$ python setup.py test

See: [Integrating with setuptools / python setup.py test / pytest-runner](https://docs.pytest.org/en/documentation-restructure/background/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner).

---

Enjoy!
