import os

def get_dirlist(path):
    """
        Return a sorted list of all enteries in path.
        This returns just the names, not the full path to the names.
    """
    final_list = [path]
    dirlist = os.listdir(path)
    for index, file in enumerate(dirlist):
        fullname = os.path.join(path, file) #Get full pathname
        if os.path.isdir(fullname):         #If a directory, recurse
            final_list += get_dirlist(fullname)
        else:
            final_list.append(os.path.join(path, file))
            
    final_list.sort()
    return final_list


def clean_up(path):
    """
        Return a sorted list of all enteries in path.
        This returns just the names, not the full path to the names.
    """
    #fpath = path + "/trash.txt"
    #open(fpath, "w")
    pathlist = get_dirlist(path)
    for path in pathlist:
        if os.path.isdir(path):         #If a directory, create trash.txt
            nfpath = path + "/trash.txt"
            #print(nfpath)
            os.remove(nfpath)


clean_up("/Users/alege/OneDrive/Desktop/pers/edu/Personal Masters/Completed Exercises/how_to_think_like_a_computer_scientist/chapter_9")        
