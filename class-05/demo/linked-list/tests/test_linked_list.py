import pytest
from linked_list.linked_list import LinkedList, Node



# Test empty linked list
def test_is_empty_ll():
    ll = LinkedList()
    expected = None
    actual = ll.head
    assert expected == actual


# Test appendig 3 values
def test_appended_3_values(ll):
    expected = f"5 -->1.33 -->Python -->{None}"
    actual = ll.__str__()
    assert expected == actual
# Test add to an existing linked list


def test_add_to_existing_ll(ll):
    expected = f"5 -->1.33 -->Python -->True -->{None}"
    ll.append(Node(True))
    actual = ll.__str__()
    assert expected == actual


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(Node(5))
    ll.append(Node(1.33))
    ll.append(Node("Python"))
    return ll