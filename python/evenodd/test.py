from evenodd import is_even, is_odd


def test_is_even_true():
    assert is_even(2) is True


def test_is_even_false():
    assert is_even(3) is False


def test_is_odd_true():
    assert is_odd(3) is True


def test_is_odd_false():
    assert is_odd(2) is False
