class Animal:
    def speak(self)->str:
        return f"Hello world"
    
    def breathe(self):
        return f"..."
    
class Dog(Animal):
    def speak(self)->str:
        return f"Woof"
    
    def play(self):
        return f"PLAY"
    
class Cat(Animal):
    def speak(self)->str:
        return f"Meow"
    
    def scratch(self):
        return f"SCRATCH"
    

class Duck(Animal):
    def speak(self)->str:
        return f"Quack"
    
    def fly(self):
        return f"FLY"


duck_One = Duck()
print(duck_One.speak())
print(duck_One.fly())
print(duck_One.breathe())