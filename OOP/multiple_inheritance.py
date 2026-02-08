class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self):
        return f"{self.name} is studying"

class Swimmer:
    def swim(self):
        return f"{self.name} is swimming"


class SwimmerStudent(Student, Swimmer):
    def __init__(self, name, age):
        super().__init__(name, age)

person_one = SwimmerStudent("John", 20)
print(person_one.swim())
print(person_one.study())