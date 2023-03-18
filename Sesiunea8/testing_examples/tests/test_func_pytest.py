from Sesiunea8.testing_examples.app.func import is_div_3_5
import pytest  # package ce trebuie instalat


def test_is_div_3_5_example():
    assert is_div_3_5(25) == 5


@pytest.mark.parametrize("n, expected", [
    (15, 35),
    (9, 3),
    (4, None)
])
def test_is_div_3_5(n, expected):
    assert is_div_3_5(n) == expected
