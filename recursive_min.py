def recursive_min(nested_list):
    """
        Find the minimum in a recursive structure of lists
        within other lists.
        Precondition: No lists or sublists are empty.
    """
    lowest = None
    first_time = True
    for element in nested_list:
        if type(element) is list:
            value = recursive_min(element)
        else:
            value = element

        if first_time or value < lowest:
            lowest = value
            first_time = False
    return lowest 

a = recursive_min([1, 2, [11, 13, [0, 3, 7]], 8])

print(a)
