import pytest
from greatest_calculator_hits_vol_2 import subtract


@pytest.mark.parametrize("x, y", [(1, 1), (4, 1), (2, 9), (4, 2), (9, 0)])
def test_subtract(x, y):
    assert subtract(x, y) == (x - y)
