import os
from importlib import import_module

try:
    import __builtin__
    builtins = __builtin__
except ImportError:  # PY3
    import builtins

BUILTINS = set(dir(builtins))

try:
    from mock import Mock
except ImportError:  # PY3
    from unittest.mock import Mock

import pytest
from _pytest.monkeypatch import MonkeyPatch


class AutoMockException(Exception):
    pass


def _mock(monkeypatch, name, module):
    if name in BUILTINS and not hasattr(module, name):
        message = "You can't mock builtin functions automatically"
        raise AutoMockException(message)
    ret = Mock()
    monkeypatch.setattr(module, name, ret)
    return ret


def _get_module(item):
    if hasattr(item.module, "MODULE"):
        return item.module.MODULE
    parts = []
    for elem in reversed(item.location[0].split(os.sep)):
        if elem == "tests":
            break
        parts.append(elem)
    parts = parts[::-1]
    # Removing the "test_" prefix and the ".py" suffix
    parts[-1] = parts[-1][5:-3]
    return import_module(".".join(parts))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item, nextitem):
    monkeypatch = MonkeyPatch()
    module = _get_module(item)
    for fname in item.fixturenames:
        if fname.startswith("mock_") and fname not in item.funcargs:
            item.funcargs[fname] = _mock(
                monkeypatch, fname[5:], module)
    yield
    monkeypatch.undo()
