def recursive_sum(nested_number_list):
    """Returns the total sum of all elements in a nested_number_list"""
    total = 0
    for element in nested_number_list:
        if type(element) is list:
            total += recursive_sum(element)
        else:
            total += element
    return total 

a = recursive_sum([1, 2, [11, [13, 5]], 8])

print(a)
