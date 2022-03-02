from fizz_buzz.fizz_buzz import fizz_buzz


def test_one():
    actual = fizz_buzz(1)
    expected = False
    assert actual == expected


def test_five():
    actual = fizz_buzz(5)
    expected = "buzz"
    assert actual == expected