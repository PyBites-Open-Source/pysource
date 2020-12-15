# PyBites Pysource

A command line tool to read Python source code.

## Installation

You can install `pybites-pysource` from [PyPI](https://pypi.org/project/pybites-pysource/):

    pip install pybites-pysource

This tool uses Python 3.x

## Usage

You can use `pybites-pysource`:

1. From the command line

		$ pysource -m re.match
		def match(pattern, string, flags=0):
			"""Try to apply the pattern at the start of the string, returning
			a Match object, or None if no match was found."""
			return _compile(pattern, flags).match(string)

	To show the resulting code with paging call `pysource` with `-p`.

2. From within Vim by selecting a `module.callable` adding this to your `.vimrc`:

		autocmd FileType python map <leader>py :exec '!python3.9 $HOME/bin/pysource.py -m <C-R><C-A> -p'<CR>

Check out [our blog post](https://pybit.es/get-python-source.html) for a demo.

## Tests

To run the tests:

	$ python setup.py test

See: [Integrating with setuptools / python setup.py test / pytest-runner](https://docs.pytest.org/en/3.0.2/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner).

---

Enjoy!
