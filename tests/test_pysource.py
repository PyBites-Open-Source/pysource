import collections
from inspect import getsource
from os.path import join
from pathlib import PurePath
from re import match
from random import sample, choice
from string import capwords
import this

import pytest

from src import get_object, print_source


@pytest.mark.parametrize("arg, expected", [
    ("random.sample", sample),
    ("pathlib.PurePath", PurePath),
    ("os.path.join", join),
    ("collections", collections),
])
def test_get_object(arg, expected):
    assert get_object(arg) is expected


@pytest.mark.parametrize("func", [
    choice,
    match,
    getsource,
    capwords,
    this  # works for modules now too
])
def test_print_source(func, capfd, source_code):
    """pager=True gives the same result in terms of output"""
    print_source(func)

    output = capfd.readouterr()[0].strip()
    actual = [line.lstrip() for line in output.splitlines()]

    src = source_code.get(func.__name__).strip()
    expected = [line.lstrip() for line in src.splitlines()]

    assert actual == expected
