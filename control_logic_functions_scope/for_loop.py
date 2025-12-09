#also known as iteration

#allows us to execute a block of code multiple times

# for loop
for i in range(5):  # iterates from 0 to 4
    print("For Loop Iteration:", i)

# iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
for number in [10, 20, 30]:
    print("Number:", number)
ages = [25, 30, 35]
for age in ages:
    print("Age:", age)  
# iterating over a tuple
for number in (1, 2, 3):
    print("Number:", number)
# iterating over a string
for char in "CBF":
    print("Character:", char)
#itterating over a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print("Key:", key, "Value:", person[key])
# iterating over dictionary items
for key, value in person.items():
    print("Key:", key, "Value:", value) 
#iterating over a set
colours = {"red", "green", "blue", "green", "purple"}  
for colour in colours:
    print("Unique Number:", number)
