import pytest

def test_exception():
    with pytest.raises(TypeError) as exc_info:
        "3" + 4
    expected_message = 'can only concatenate str (not "int") to str'
    assert str(exc_info.value) == expected_message
