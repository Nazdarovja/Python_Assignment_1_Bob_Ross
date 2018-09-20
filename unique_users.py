from Utility.Textfile2json import convert
import os

def unique_users(data):
    """Gets the amount of unique names in data

        Args:
            data: List of Dictionaries

        Returns:
            int, unique names
    """
    
    # parse all names out of dictionary to list
    names = []
    for dct in data:
        names.append(dct['name'])
    
    # creating a set, with the list of names as input. 
    # this will ignore all names which is already contained in the set,
    # only containing unique entries in the end.
    unique_names = set(names)

    return len(unique_names)


if __name__ == '__main__':
    file_name = 'BobRoss.txt'
    data = convert(file_name)
    print(unique_users(data))
