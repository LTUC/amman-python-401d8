from recursion import __version__
from recursion.factorial import fact


def test_fact_five():
    expected = 120
    actual = fact(5)
    assert expected == actual



def test_value_is_numeric_false():
    expected = "Please provide a positive integer"
    actual = fact("5")
    assert actual == expected