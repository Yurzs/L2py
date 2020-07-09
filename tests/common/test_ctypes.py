import pytest


@pytest.mark.parametrize(["input", "shift", "output"], [
    (249, 8, 8)
])
def test_Int8lshift(input, shift, output):
    pass