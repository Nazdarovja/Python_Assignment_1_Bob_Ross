def get_number_of_ruined(json_data):
    count = 0

    for line in json_data:
        if "ruined" in ''.join(line).lower():
            count += 1


    return count
