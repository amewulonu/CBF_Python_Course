# a = 5
# b = 0
# print(a/b)

#try, except, else, finally example

# try:
#     a = 5
#     b = 1
#     print(a/b)
# except ZeroDivisionError as e:
#     print("You can't divide by zero!", e)
# else:
#     print("Division performed successfully!")
# finally:
#     print("Execution completed.")

# try:
#     print(a)
# except Exception as e:
#     print("something went wrong with printing that variable")
#     print(e)


# try:
#     a = float(input("Enter a number: "))
#     b = float(input("Enter another number: "))
#     result = a / b
# except ZeroDivisionError:
#     print("Error: You can't divide by zero!")
# except TypeError:
#     print("Error: Please enter valid numbers.")
# except ValueError:
#     print("Error: Invalid input. Please enter numeric values.")
# except Exception as e:
#     print("An unexpected error occurred:", e)
# else:
#     print("Result:", result)
#     print("Division performed successfully!")
# finally:
#     print("Thank you for using the division program.")

# try:
#     raise Exception("This is a custom exception message.")
# except Exception as e:
#     print("Caught an exception:", e)

# import math

# try:
#     print(math.exp(1000))  
# except OverflowError:
#     print("Value is too large to compute.")
# except Exception as e:
#     print(f"Unexpected error: {e}")

## AttributeError
# class Animal:
#     def __init__(self, name: str):
#         self.name = name

#     def speak(self) -> str:
#         return f"{self.name} makes a sound."


# animal_one = Animal("GenericAnimal")
# print("Speak", animal_one.speak())
# print("Breathe", animal_one.breathe())


## KeyError
# person_one = {"name": "Alice", "age": 30}
# print(person_one["name"])
# print(person_one["address"])


# ## AssertionError

# try:
#     assert 1 == 2, "Assertion failed"
# except AssertionError as e:
#     print(e)


# ## IndexError
# my_list = [1, 2, 3]

# try:
#     element = my_list[5]
# except IndexError as e:
#     print(e)


# MemoryError
# try:
#     li = [1] * (10**10)
# except MemoryError as e:
#     print(e)