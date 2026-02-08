class Animal:
    def speak(self)->str:
        return f"Hello world"
    
    def breathe(self):
        return f"..."

class Feline(Animal):
    species = "Feline!"

class Cat(Feline):
    def meow(self):
        return f"Meow!"
    

cat_one = Cat()
print(cat_one.meow())
print(cat_one.breathe())
print(cat_one.speak())
print(cat_one.species)