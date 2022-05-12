import pytest
from greatest_calculator_hits_vol_2 import divide


@pytest.mark.parametrize("x, y", [(1, 1), (4, 1), (2, 9), (4, 2)])
def test_divide(x, y):
    assert divide(x, y) == (x / y)


@pytest.mark.parametrize("x, y", [(9, 0)])
def test_divide_with_division_by_zero(x, y):
    with pytest.raises(ZeroDivisionError):
        divide(x, y)
