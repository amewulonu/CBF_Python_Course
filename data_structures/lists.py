# creating lists using square brackets
names = ["Alice", "Bob", "Charlie", "Diana"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
print("Names List:", names)
print("Numbers List:", numbers)
print("Mixed List:", mixed)

# # create a list using the list() constructor
# weather_list = list(("sunny", "rainy", "cloudy"))
# print("Weather List:", weather_list)

# convert a string to a list of characters
# print(list("hello"))

# # create a list with repeated elements
shopping_list = ["eggs"] * 3
print("Shopping List:", shopping_list)
number_list = [0] * 5
print("Number List:", number_list)

#create a list from a tuple
tuple_data = (10, 20, 30)
tuple_list = list(tuple_data)
print("List from Tuple:", tuple_list)

# create a list from a set
set_data = {"apple", "banana", "cherry"}
set_list = list(set_data)
print("List from Set:", set_list)

# # accessing list elements using indexing
print("First element in names:", names[0])
#numbers = [1, 2, 3, 4, 5]
print("Last element in numbers:", numbers[-1])

# #appening elements to a list, means adding an element to the end of the list
# names = ["Alice", "Bob", "Charlie", "Diana"]
names.append("Eve")
print("Updated Names List after append:", names)
names.append(["Frank", "Grace"])
print("Updated Names List after appending a list:", names)
names.extend(["Hannah", "Ian"])
print("Updated Names List after extend:", names)
names.extend("JKL")
print("Updated Names List after extending with string:", names)
names.extend({"M", "N"})
print("Updated Names List after extending with set:", names)
names.extend(("O", "P"))
print("Updated Names List after extending with tuple:", names)

# inserting elements at a specific index
# numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
print("Updated Numbers List after insert:", numbers)
numbers.insert(0, [0, 1, 3])
print("Updated Numbers List after inserting a list:", numbers)
numbers.insert(-1, 4.5)
print("Updated Numbers List after inserting at -1 index:", numbers)
numbers.insert(5, (3.5, 3.75))
print("Updated Numbers List after inserting a tuple:", numbers)
numbers.insert(len(numbers), 6)
print("Updated Numbers List after inserting at the end:", numbers)
numbers.insert(100, 7)
print("Updated Numbers List after inserting at out-of-bounds index:", numbers)

# removing elements from a list by value
# mixed = [1, "two", 3.0, True, "two"]
mixed.remove("two")
print("Mixed List after remove:", mixed)
# mixed.remove("not_in_list")  # This would raise a ValueError

# removing elements from a list by index
# numbers = [1, 2, 2.5, 3, 4, 5, (3.5, 3.75), 6, 7]
removed_element = numbers.pop(2)
print("Removed Element:", removed_element)
print("Numbers List after pop:", numbers)
removed_last = numbers.pop()
print("Removed Last Element:", removed_last)
print("Numbers List after popping last element:", numbers)
removed_first = numbers.pop(0)
print("Removed First Element:", removed_first)
print("Numbers List after popping first element:", numbers)

#clear all elements from a list
mixed = [1, "two", 3.0, True]
mixed.clear()
print("Mixed List after clear:", mixed)

#other list operations
# concatenation
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
combined_list = list1 + list2
print("Combined List:", combined_list)  

# reversal
list1.reverse()
print("Reversed List1:", list1)
# sorting
unsorted_list = [5, 2, 9, 1, 5, 6]
unsorted_list.sort()
print("Sorted List:", unsorted_list)
#can also sort in descending order
unsorted_list.sort(reverse=True)
print("Sorted List in Descending Order:", unsorted_list)
# length 
print("Length of Names List:", len(names))
# membership testing
print("Is 'Alice' in Names List?", "Alice" in names)
#slicing
sliced_names = names[1:4]
print("Sliced Names List (index 1 to 3):", sliced_names)
# slicing with step
sliced_numbers = numbers[::2]
print("Sliced Numbers List with step 2:", sliced_numbers)
# negative indexing and slicing
last_two_names = names[-2:]
print("Last two names in Names List:", last_two_names)
# negative step slicing
reversed_numbers = numbers[::-1]
print("Reversed Numbers List using slicing:", reversed_numbers)
#negative step with specific indices
neg_step_slice = names[4:1:-1]
print("Names List sliced with negative step (index 4 to 2):", neg_step_slice)

# deleting a list
del unsorted_list
# print("Unsorted List after delete:", unsorted_list)  # This will raise an error since 'unsorted_list' is deleted
print("Unsorted List has been deleted and cannot be accessed.")

#counting occurrences of an element
names = ["Alice", "Bob", "Charlie", "Diana", "Alice", "Bob"]
alice_count = names.count("Alice")
print("Number of times 'Alice' appears in Names List:", alice_count)
#finding index of an element
first_bob_index = names.index("Bob")
print("Index of first occurrence of 'Bob' in Names List:", first_bob_index)
#finding index of an element with start and end parameters
second_bob_index = names.index("Bob", first_bob_index + 1)
print("Index of second occurrence of 'Bob' in Names List:", second_bob_index)  

# copying a list
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print("Original List:", original_list)
print("Copied List:", copied_list)
print(id(original_list), id(copied_list))  # Different memory addresses 
print("Are both lists equal?", original_list == copied_list)  # True
print("Are both lists the same object?", original_list is copied_list)  # False







