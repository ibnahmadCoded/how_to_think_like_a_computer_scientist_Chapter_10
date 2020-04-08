def count_target(nested_list, target):
    """
        Returns the number of target in a nested list
    """
    count = 0
    for element in nested_list:
        if type(element) is list:
            count += count_target(element, target)
        else:
            if element == target:
                count += 1
    return count

a = count_target(([1, 2, [11, 13, 8], 8]), 8)

print(a)
                 
            
