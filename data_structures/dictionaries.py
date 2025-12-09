# a mapping of key to value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    30: True, 
}


#keys of a dictionary must be immutable data types like strings, numbers, or tuples, not lists, sets, or other dictionaries.

print("person", person)
# accessing values by key
# print( person["name"])  # Output: Alice
# print(person.get("age"))  # Output: 30
# print( person[30])  # Output: True

# another_dict = dict(country="USA", profession="Engineer", hobby="Painting", age=25, address={"street": "123 Main St", "zip": "10001"}, is_student=False)
# print("another_dict", another_dict)


# adding or updating key-value pairs
person["email"] = "example@python.c.uk"
person["address"] = {"street": "123 Main St", "zip": "10001"}
person[100] = False
person["age"] = 31  # updating existing key
print("Updated my_dict:", person)

# # # removing key-value pairs
del person["city"]
removed_value = person.pop("age")
print("Removed age:", removed_value)
print("person after removals:", person)

popped_item = person.popitem()  # removes and returns an arbitrary (key, value) pair
print("Popped item:", popped_item)
print("person after popitem:", person)
person.clear()
print("After Clearing person:", person)

# dictionary methods
sample_dict = {"a": 1, "b": 2, "c": 3}
print("Keys:", sample_dict.keys())
print("Values:", sample_dict.values())
print("Items:", sample_dict.items())


