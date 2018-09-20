import os

def convert(textfile):
    """Take a .txt file as input. Returns a list of json objects in the format {timestamp, name, message}"""

    list_of_lines_as_json = []

    with open(textfile, 'r', encoding='utf8') as fp:

        for line in fp:
            # remove line separation, should work on any OS
            org_line = line.rstrip(os.linesep)
            # max 2 splits, to avoid splitting messages >1 word
            sep = org_line.split(" ", 2)
            sep_timestamp, sep_name, sep_message = sep
            line_as_json = {
                "timestamp": sep_timestamp,
                "name": sep_name[:-1],          # remove :
                "message": sep_message
            }
            list_of_lines_as_json.append(line_as_json)
    return list_of_lines_as_json
