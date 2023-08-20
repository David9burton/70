def unique_elements(lst):
    """Return a list of unique elements from the input list."""
    return list(set(lst))

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 6, 7, 8, 8, 9, 1]
print(f"Original list: {my_list}")
print(f"Unique elements are: {unique_elements(my_list)}")
