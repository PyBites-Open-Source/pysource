import pytest

choice = '''
def choice(self, seq):
    """Choose a random element from a non-empty sequence."""
    # raises IndexError if seq is empty
    return seq[self._randbelow(len(seq))]
'''
match = '''
def match(pattern, string, flags=0):
    """Try to apply the pattern at the start of the string, returning
    a Match object, or None if no match was found."""
    return _compile(pattern, flags).match(string)
'''
getsource = '''
def getsource(object):
    """Return the text of the source code for an object.

    The argument may be a module, class, method, function, traceback, frame,
    or code object.  The source code is returned as a single string.  An
    OSError is raised if the source code cannot be retrieved."""
    lines, lnum = getsourcelines(object)
    return ''.join(lines)
'''
SOURCE_CODE = dict(
    choice=choice,
    match=match,
    getsource=getsource
)


@pytest.fixture(scope='module')
def source_code():
    return SOURCE_CODE
