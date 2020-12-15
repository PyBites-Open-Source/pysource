import importlib
import inspect
import pydoc


def get_callable(arg):
    module_str, name = arg.rsplit(".", 1)
    module = importlib.import_module(module_str)
    return getattr(module, name)


def print_source(func, pager=False):
    output = pydoc.pager if pager else print
    output(inspect.getsource(func))
