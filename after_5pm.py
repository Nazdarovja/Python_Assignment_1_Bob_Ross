def after_5pm(json_data):
    """
    Takes list of json as input. Returns number chat messages after 17/5pm.
    """
    counter = 0
    for line in json_data:
        if(int(line['timestamp'][11:13]) >= 17 or int(line['timestamp'][11:13]) < 4 ):  # between 17-03 (where dataset stops)
            counter += 1

    return counter

