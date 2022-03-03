# Recursion

Factorial!
5!= 5*4*3*2*1 --> 120
5! = 5*4!

4!=4*3*2*1 --> 24
4! = 4*3!

A recursive function solves a problem by dividing it into subproblems, those subproblems follows the same pattern.

```python
    def factorial(value):
        # Base case
        if value <= 1:
            return 1
        #general case
        return value*factorial(value-1)
```

factorial(5):
    is 5<=1?

    return 5*factorial(5-1) --> 120

                factorial(4):
                    is 4<=1?

                    retrun 4*factorial(4-1)

                              factorial(3):
                                is 3<=1?
                                return 3* factorial(3-1)

                                            factorial(2):
                                                is 2<=1?
                                                return 2*factorial(2-1)
                                                          factorial(1):
                                                            is 1<=1?
                                                            return 1
