from file_io.read_file import read_file


def test_read_file():
    """
        Hello Python devs
        Let's write some code
        Third line is here
    """
    expected = "Hello Python devs\nLet's write some code\nThird line is here"
    actual = read_file("file_io/assets/spam.txt")
    assert expected == actual