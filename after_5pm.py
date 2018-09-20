from Utility.Textfile2json import convert


def after_5pm(file_name):
    """
    Takes -txt filename as input. Returns number chat messages after 17/5pm.
    """
    json_list = convert(file_name)
    counter = 0
    for line in json_list:
        if(int(line['timestamp'][11:13]) == 17):
            counter += 1

    return counter

if __name__ == '__main__':
    file_name = 'BobRoss.txt'
    after_5pm(file_name)
