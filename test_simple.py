from simple import add, subtract, multiply, divide


def test_add():
    assert add(4, 5) == 9


def test_subtract():
    assert subtract(10, 2) == 8


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(10, 2) == 5
    try:
        divide(10, 0)
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        assert True
