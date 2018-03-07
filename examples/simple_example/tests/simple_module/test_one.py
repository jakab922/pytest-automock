try:
    import mock
except ImportError:  # PY3
    from unittest import mock

from simple_module.one import func2, func


def test_func2(mock_STUFF):
    """
    You can mock module level variables.
    """
    assert func2() == mock_STUFF
