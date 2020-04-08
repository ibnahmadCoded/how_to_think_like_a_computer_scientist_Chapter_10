def flatten(nested_list):
    """
        Returns all the of nested list in a simple list.
    """
    flat = []
    for element in nested_list:
        if type(element) is list:
            flat += flatten(element)
        else:
            flat.append(element)
    return flat

a = flatten([1, 2, [11, [9, 5, 100], 13, 8], 8])

print(a)
                 
