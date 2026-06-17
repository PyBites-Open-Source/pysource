import importlib
import inspect
import pydoc


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
    # Several stdlib modules (datetime, decimal, ...) expose C objects whose
    # __module__ points at a shim with no source; the Python source lives in a
    # _py<module> sibling.
    module_name = getattr(obj, "__module__", None)
    name = getattr(obj, "__name__", None)
    if not module_name or not name:
        return None
    try:
        module = importlib.import_module(f"_py{module_name}")
    except ImportError:
        return None
    pure = getattr(module, name, None)
    if pure is None:
        return None
    try:
        return inspect.getsource(pure)
    except (OSError, TypeError):
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
