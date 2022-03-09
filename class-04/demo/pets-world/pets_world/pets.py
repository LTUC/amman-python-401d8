from abc import ABC, abstractmethod


class Pet:
    count = 0
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        Pet.count+=1

    def __str__(self):
        return f'My name is: {self.name}'
    
    def __repr__(self):
        return f'I am a representation for {self.name}'

    def sleep(self):
        return f'{self.name} is sleeping!'
    
    @abstractmethod
    def speak(self):
        pass

    @classmethod
    def get_pets_count(cls):
        return cls.count
    

class Cat(Pet):
    
    # *args, **kwargs
    def __init__(self,name, age, breed, color):
        self.color = color
        super().__init__(name, age, breed)

    def speak(self):
        return f'{self.name} says: Mewooooo'

    def pur(self):
        return f'{self.name} is purrrrrring!!!'

class Dog(Pet):

    def speak(self):
        return f'{self.name} says: Wooofffff'
    
    @staticmethod
    def get_average_dog_age():
        return "The average age of a dog is 10 years"

if __name__ == "__main__":

    lulua = Cat("Lulua", 8, "Himalyan", "Grey")
    # juliano = Cat("Juliano", 3, "Chenchila")
    oscar = Dog("Oscar", 2, "Husky")
    print(lulua)
    print(lulua.age)
    print(lulua.color)
    print(lulua.breed)
    print(lulua.pur())
    # print(type(lulua))
    # print(juliano.speak())
    # print(type(juliano))
    print(oscar.speak())
    print(f'Count: {Pet.get_pets_count()}')
    print(f'average dog age: {Dog.get_average_dog_age()}')

    # print(type(Oscar))
    
