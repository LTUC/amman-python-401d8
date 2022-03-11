from linked_list import LinkedList
from node import Node

if __name__ == "__main__":
    ll = LinkedList()
    mustafa = Node("Mustafa")
    zaid = Node("Zaid")
    hind = Node("Hind")
    ll.append(mustafa)
    ll.append(zaid)
    ll.append(hind)

    current = ll.head
    while (current.value != "Zaid"):
        current = current.next
    print(current.value)
