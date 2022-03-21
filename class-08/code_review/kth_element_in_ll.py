from linked_list import LinkedList

def kth_element(k):

    ll= LinkedList()

    """
    head -> [1] -> [3] -> [8] -> [2] -> X
    """
    if k < 0 or k >= ll.length:
        return "Error"
    
    count = ll.length - 1
    current = ll.head
    while current:
        if k == count:
            return current.value
        current = current.next
        count = count - 1

