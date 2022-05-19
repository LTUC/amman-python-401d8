

class HashaTable(object):
    def __init__(self, size = 1024):
    
        self.size = size
        self.map = [None]*size
        # self.map = [[]]*size
        # self.map = [LinkedList()]*size
    def _get_hash(self, key):
        """
        - ascii code of a key summation
        - encode chars in key into oct and add it to ascii sum
        - Prime = 19 then multiply it by ascii sum
        - mod the result over self.size
        - return the hashed value
        """
        # Hello
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch) #86
            sum_of_ascii+=ch_ascii
        hashed_key = (sum_of_ascii*19)%self.size

        return hashed_key

    def add(self, key, value):
    # def __setitem__(self, key, value):
        # get index from get_hash
        idx = self.get_hash(key)
        # check if the bucket at that index is empty, add the value there
        if not self.map[idx]:
            self.map[idx] = [[key, value]] # LinkedList().add({key, value})
        # if the bucker is not empty, append, add to the sotrage object(collision)
        else:
            self.map[idx].append([key, value])


    def contains(self):
        pass

    # def find(self, key):
    def __getitem__(self, key):
        # call the get hash method and send the key to it
        idx = self.get_hash(key)
        # get that index and look it up from the map
        # return the value stroed in that index
        return self.map[idx][0][1]

if __name__ == "__main__":
    hashtable = HashaTable()
    hashtable.add("cloud", "AWS")
    hashtable.add("cloud", "Azure")
    hashtable.add("could", "Rainy")
    hashtable.add("name", "Python")
    print(hashtable["name"])



    # for item in enumerate(hashtable.map):
    #     if item is not None:
    #         print(item)

