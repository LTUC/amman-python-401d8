# Zip two linked lists

```python

    def zipped_ll(ll1, ll2):
        ll1_current = ll1.head
        ll2_current = ll2.head

        """
          - loop thorugh ll2
          - if the ll1 current is empty and the ll2 current is not empty:
                - append ll2 to ll1
          - insert after ll1.head 
          1 -> 2 -> 3
          4 ->5 ->6
        """
        while (ll1_current and ll2_current != Null):
            ll1_next = ll1_current.next
            ll2_next = ll2_current.next
            ll1_current.next = ll2_current
            ll1_current = ll1_next
            if ll1_current != Null:
                ll2_current.next = ll1_current
            
            ll2_current = ll2_next
        return ll1
```