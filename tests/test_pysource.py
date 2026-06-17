import collections
import datetime
import decimal
import sys
from inspect import getsource
from os.path import join
from pathlib import PurePath
from re import match
from random import sample, choice
from string import capwords
import this

import pytest

from pysource import (
    SourceUnavailableError,
    get_object,
    get_source,
    print_source,
)
from pysource.__main__ import main


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("random.sample", sample),
        ("pathlib.PurePath", PurePath),
        ("os.path.join", join),
        ("collections", collections),
    ],
)
def test_get_object(arg, expected):
    assert get_object(arg) is expected


@pytest.mark.parametrize(
    "func",
    [
        choice,
        match,
        getsource,
        capwords,
        this,  # works for modules now too
    ],
)
def test_print_source(func, capfd, source_code):
    """pager=True gives the same result in terms of output"""
    print_source(func)

    output = capfd.readouterr()[0].strip()
    actual = [line.lstrip() for line in output.splitlines()]

    src = source_code.get(func.__name__).strip()
    expected = [line.lstrip() for line in src.splitlines()]

    assert actual == expected


def test_get_source_returns_source_for_python_object():
    assert get_source(get_source).lstrip().startswith("def get_source")


@pytest.mark.parametrize(
    "obj, head",
    [
        (datetime.date, "class date"),  # _pydatetime sibling
        (decimal.Decimal, "class Decimal"),  # _pydecimal sibling
    ],
)
def test_get_source_falls_back_to_pure_python(obj, head):
    assert get_source(obj).lstrip().startswith(head)


def test_get_source_raises_when_no_python_source():
    with pytest.raises(SourceUnavailableError, match="len"):
        get_source(len)


def test_get_source_raises_for_object_without_source():
    with pytest.raises(SourceUnavailableError, match="42"):
        get_source(42)


def test_main_prints_source(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["pysource", "-m", "re.match"])
    main()
    assert "def match" in capsys.readouterr().out


def test_main_exits_with_friendly_error(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["pysource", "-m", "builtins.len"])
    with pytest.raises(SystemExit) as exc:
        main()
    assert "no Python source available" in str(exc.value)
