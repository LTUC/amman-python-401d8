from pets_world.pets import (
                                Pet,
                                Dog,
                                Cat
                            )
import pytest


# Count of pets
def test_pets_count(data):
    expected = 4
    actual = Pet.get_pets_count()
    assert expected == actual


#Cats are purring
def test_cat_pur(data):
    assert data[0].pur() == f'Cat1 is purrrrrring!!!'
    assert data[1].pur() == f'Cat2 is purrrrrring!!!'


#Dogs age
def test_dog_pur(data):
    assert data[2].age == 5
    assert data[3].age == 1


@pytest.fixture
def data():
    cat1 = Cat("Cat1", 2, "breed1", "green")
    cat2 = Cat("Cat2", 3, "breed2", "Blue")
    dog1= Dog("Dog1", 5, "breed3")
    dog2= Dog("Dog2", 1, "breed4")
    return [cat1, cat2, dog1, dog2]