from Utility.Textfile2json import convert
import os

def unique_users(text_file):
    """
        Takes -txt filename as input. Returns number of unique users.
    """
    # read text_file in convert() which returns a dictionary
    json_data = convert(text_file)

    # parse all names out of dictionary to list
    names = []
    for dct in json_data:
        names.append(dct['name'])
    
    # creating a set, with the list of names as input. 
    # this will ignore all names which is already contained in the set,
    # only containing unique entries in the end.
    unique_names = set(names)

    return len(unique_names)


if __name__ == '__main__':
    file_name = 'BobRoss.txt'
    unique_users(file_name)
