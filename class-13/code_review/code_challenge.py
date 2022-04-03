from queue import Queue


class Dog:
    pass


class Cat:
    pass


class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()
        # self.animals = Queue()

    def enqueue(self, animal):
        if type(animal) == Dog:
            self.dogs.enqueue(animal)
        self.cats.enqueue(animal)
        self.animals.enqueue(animal)
    
    def dequeue(self, pref = None):
        if not pref:
            animal = self.animals.dequeue()
            if type(animal) is Dog:
                self.dogs.dequeue()
            else:
                self.cats.dequeue()
            return animal
        # animal queue = [cat, cat, dog, cat,cat]
        if pref == 'cat':
            cat = self.cats.dequeue()
            return cat
        if pref == 'dog':
            dog = self.dogs.dequeue()

            return dog


'[{(])}]'