import pytest
from operator import add

sample_test_cases = [
    # (x, y, result)
    (1, 2, 3),
    (0, 0, 0),
    (-1, 2, 1),
]

@pytest.mark.parametrize("x,y,result", sample_test_cases)
def test_add(x, y, result):
    assert add(x, y) == result
