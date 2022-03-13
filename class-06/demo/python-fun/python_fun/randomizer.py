from platform import python_branch
import random
from collections import Counter

def randmoizer():
    return random.randint(1, 6)

if __name__ == "__main__":
    my_dict = {
        "5":5,
        "3":3,
        "2":2,
        "1":1,
        "9":9
    }
    my_tuple = (5,3,2,3,5,1,9)
    # rolls = tuple([randmoizer() for _ in range(6)])
    ctr = Counter(my_tuple)
    # [(5, 2), (3, 2), (2, 1), (1, 1), (9, 1)]
    # print(rolls)
    # print(ctr[3])
    # print(ctr["yhayha"])
    # print(my_dict.items())
    # print(ctr.values())
    # print(ctr.keys())
    print(my_dict["yahya"])
    # print(ctr.most_common()[0][0])
    # print(ctr.most_common()[4][0])

