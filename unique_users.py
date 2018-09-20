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

    # creating a set, with the list of names as input. 
    # this will ignore all names which is already contained in the set,
    # only containing unique entries in the end.
    return len(set([dct['name'] for dct in data]))


if __name__ == '__main__':
    file_name = 'BobRoss.txt'
    data = convert(file_name)
    print(unique_users(data))
