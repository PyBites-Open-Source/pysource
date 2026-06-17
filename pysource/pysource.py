import importlib
import inspect
import linecache
import pydoc
import re


class SourceUnavailableError(Exception):
    pass


def get_object(arg):
    module_str, sep, name = arg.rpartition(".")
    if sep:
        module = importlib.import_module(module_str)
        return getattr(module, name)
    else:
        return importlib.import_module(name)


def _pure_python_source(obj):
    # A few stdlib modules (datetime, decimal, io) ship a C implementation and
    # keep the Python source in a _py<module> sibling. The pure objects there
    # still carry __module__ of the shim, so inspect.getsource looks in the
    # wrong file; read the sibling file directly instead.
    module_name = getattr(obj, "__module__", None)
    name = getattr(obj, "__name__", None)
    if not module_name or not name:
        return None
    try:
        module = importlib.import_module(f"_py{module_name}")
    except ImportError:
        return None
    source_file = getattr(module, "__file__", None)
    if getattr(module, name, None) is None or source_file is None:
        return None
    definition = re.compile(rf"^(async\s+def|def|class)\s+{re.escape(name)}\b")
    lines = linecache.getlines(source_file)
    for index, line in enumerate(lines):
        if definition.match(line):
            return "".join(inspect.getblock(lines[index:]))
    return None


def get_source(obj):
    try:
        return inspect.getsource(obj)
    except (OSError, TypeError):
        source = _pure_python_source(obj)
        if source is not None:
            return source
        name = getattr(obj, "__name__", repr(obj))
        raise SourceUnavailableError(
            f"no Python source available for {name!r} "
            "(likely implemented in C / a builtin)"
        )


def print_source(func, pager=False):
    output = pydoc.pager if pager else print
    output(get_source(func))
