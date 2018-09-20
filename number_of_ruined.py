def get_number_of_ruined(json_data):
    """
    Counts all occurances of the word "ruined" in input json data (upper- and lowercased) and returns the count
    """

    count = 0
    for line in json_data:
        to_check = line["name"] + ' ' + line["message"]
        word_list = to_check.split(' ')
        
        for word in word_list:
            if "ruined" in word.lower():
                count += 1

    return count
