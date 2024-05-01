
def test_function():
    result = 1 + 2
    assert result == 3


def test_failing_test():
    result = 1 + 2
    assert result == 4


def test_not_equals():
    bad_result = 'not this'
    assert 'actual result' != bad_result

def test_comparisons():
    result = 6
    assert result > 5
    assert result < 9
    assert result >= 6
    assert result <= 6


def test_is_not_operator():
    expected = object()
    actual = object()

    assert actual is not expected


def test_is_operator():
    expected = object()
    actual = expected

    assert actual is expected
