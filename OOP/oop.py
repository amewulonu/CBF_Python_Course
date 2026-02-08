class Animal:

    def speak(self)->str:
        return f"Hello world"
    
    def breathe(self):
        return f"..."

class Dog(Animal):
    species = "Canis familiaris"  # Class attribute shared by all instances

    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__id = "ABX"

    def __repr__(self):
        return f"Dog(name='{self.name} age={self._age})"

    def bark_simple(self):
        return f"Woof!"
         
    def bark_name(self):
        return f"{self.name} says Woof!"
    
    @property
    def age(self):
        return self._age 

    def set_age(self, new_age):
        self._age = new_age
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def set_id(self, new_id):
        self.__id = new_id


def speak(self) -> str:
    return f"Woof! {super().speak()}"


    


dog_test: Animal = Dog("Charlie", 5)
print("Speak", dog_test.speak())
print("Breathe", dog_test.breathe())

dog_one = Dog("Buddy", 3)
print("Dog Name:", dog_one.name)
print("Dog Age:", dog_one._age)
# print(dog_one.bark_simple())
# print(dog_one.bark_name())
# print(dog_one)

# print(dog_one.__id)
print("id", dog_one.id)
dog_one.set_id = "ABC"
print(dog_one.id)

# dog_one = Dog("Buddy", 3)
# print(dog_one._Dog__id)

# dog_two = Dog("Max", 5)
# print("Dog Name:", dog_two.name)
# print("Dog Age:", dog_two.age)

# dog_three = Dog("Buddy", 3)
# print(id(dog_one))
# print(id(dog_two))
# print(id(dog_three))
# print(dog_three.name == dog_one.name)
# print(dog_three is dog_one)




# class Frog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# marsh_frog = Frog("Marsh", 2)
# print("Frog Name:", marsh_frog.name)

# class Bike:
#     name = "A bike"

# bike_one = Bike()
# print(bike_one.name)
# bike_two = Bike()
# print(bike_two.name)