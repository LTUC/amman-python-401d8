# from node import Node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, node):
        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty linked list"
        else:
            current = self.head
            while(current):
                output+= f'{current.value} -->'
                current = current.next
            
            output+= "None"
        return output

"""
item1=1
item2= "Hello"
item3= False
1->"Hello"->False->None
"""

if __name__ == "__main__":
    ll = LinkedList()
    mustafa = Node("Mustafa")
    zaid = Node("Zaid")
    hind = Node("Hind")
    ll.append(mustafa)
    ll.append(zaid)
    ll.append(hind)
    print(ll)

