try:
    import mock
except ImportError:  # PY3
    from unittest import mock

from simple_module.level_two.other import other_func


def test_other_func(mock_func):
    """
    You can mock functions imported from a different
    module.
    """
    mock_func.return_value = mock.sentinel.retval

    ret = other_func(mock.sentinel.a, mock.sentinel.b)

    mock_func.assert_called_once_with(
        mock.sentinel.a)

    assert ret == (mock.sentinel.b, mock.sentinel.retval)
