numbers_set = {1, 2, 3, 4, 5}
print("Numbers Set:", numbers_set)
fruits_set = {"apple", "banana", "cherry"}
print("Fruits Set:", fruits_set)
mixed_set = set((1, "two", 3.0, (4, 5)))
#can create a set from a tuple using the set() constructor
print("Mixed Set:", mixed_set)
names_set = set(["Alice", "Bob", "Charlie"])
#can create a set from a list using the set() constructor
print("Names Set:", names_set)


cbf_set = {"CBF", "CBFFest", "CBF", "CBF Python"}
# even though "CBF" is repeated, sets store only unique elements
print("CBF Set (with duplicates):", cbf_set)

# # adding elements to a set
cbf_set.add("New Element")
print("CBF Set after adding an element:", cbf_set)  
#adding a duplicate element has no effect
cbf_set.add("CBF")
print("CBF Set after adding a duplicate element:", cbf_set) 
#adding multiple elements using update()
cbf_set.update(["Another Element", "Yet Another Element"])
print("CBF Set after updating with multiple elements:", cbf_set)
# can add hashable types like tuples to a set, hasable types are immutable and include strings, numbers, and tuples
cbf_set.add( ("TupleElement1", "TupleElement2") )
print("CBF Set after adding a tuple element:", cbf_set)
# adding a set to a set using update()
cbf_set.update( {"SetElement1", "SetElement2"} )
print("CBF Set after adding set elements using update():", cbf_set)

#cannot add a list or dictionary to a set as they are unhashable types

#check membership of an element in a set
print("Is 'CBF' in CBF Set?", "CBF" in cbf_set)
print("Is 'NonExistent' in CBF Set?", "NonExistent" in cbf_set)
print("Is 'NonExistent' not in CBF Set?", "NonExistent" not in cbf_set)

# # removing elements from a set
cbf_set.remove("CBFFest")  # raises KeyError if element not found
print("CBF Set after removing 'CBFFest':", cbf_set)
cbf_set.discard("NonExistentElement")  # does not raise an error if element not found
print("CBF Set after discarding 'NonExistentElement':", cbf_set)
popped_element = cbf_set.pop()  # removes and returns an arbitrary element
print("Popped Element:", popped_element)
print("CBF Set after popping an element:", cbf_set) 

# # set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Set A:", set_a)
print("Set B:", set_b)
# union
set_union = set_a | set_b
print("Union of Set A and Set B:", set_union)
# intersection
set_intersection = set_a & set_b
print("Intersection of Set A and Set B:", set_intersection)
set_intersection_two = set_a.intersection(set_b)
print("Intersection of Set A and Set B using intersection() method:", set_intersection_two)

# # # difference
set_difference = set_a - set_b
print("Difference of Set A and Set B (A - B):", set_difference)
set_difference_two = set_a.difference(set_b)
print("Difference of Set A and Set B using difference() method (A - B):", set_difference_two)

set_difference_ba = set_b - set_a
print("Difference of Set B and Set A (B - A):", set_difference_ba)
set_difference_ba_two = set_b.difference(set_a)
print("Difference of Set B and Set A using difference() method (B - A):", set_difference_ba_two)

# # symmetric difference
set_sym_diff = set_a ^ set_b
print("Symmetric Difference of Set A and Set B:", set_sym_diff)
set_sym_diff_two = set_a.symmetric_difference(set_b)
print("Symmetric Difference of Set A and Set B using symmetric_difference() method:", set_sym_diff_two)


# # set methods
print("Set A is disjoint with Set B?", set_a.isdisjoint(set_b))
print("Set A is subset of Set B?", set_a.issubset(set_b))
print("Set A is superset of Set B?", set_a.issuperset(set_b))
print("Length of Set A:", len(set_a))
cleared_set = set_a.copy()
cleared_set.clear()
print("Cleared Set A copy:", cleared_set)