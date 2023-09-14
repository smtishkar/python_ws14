import pytest
from rectangle import Rectangle


@pytest.fixture
def r1():
    return Rectangle(length_cm=2)


@pytest.fixture
def r2():
    return Rectangle(length_cm=2, width_cm=4)


@pytest.fixture
def r3():
    return Rectangle(length_cm=2)


def test_step_1(r1, r3):
    assert r1 == r3


def test_step_2(r1, r2):
    assert r1 != r2


if __name__ == "__main__":
    pytest.main()