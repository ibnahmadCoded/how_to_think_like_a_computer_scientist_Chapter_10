import os

def get_dirlist(path):
    """
        Return a sorted list of all enteries in path.
        This returns just the names, not the full path to the names.
    """
    final_list = []
    dirlist = os.listdir(path)
    for index, file in enumerate(dirlist):
        fullname = os.path.join(path, file) #Get full pathname
        if os.path.isdir(fullname):         #If a directory, recurse
            final_list += get_dirlist(fullname)
        else:
            final_list.append(os.path.join(path, file))
            
    final_list.sort()
    return final_list

print(get_dirlist("/Users/alege/OneDrive/Desktop/pers/edu/Personal Masters/Completed Exercises/how_to_think_like_a_computer_scientist/chapter_9"))            
