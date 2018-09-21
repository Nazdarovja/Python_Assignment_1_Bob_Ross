def after_5pm(json_data):
    """
    Takes list of json as input. Returns number chat messages after 17/5pm.
    """
    return len([(int(line['timestamp'][11:13]) >= 17 or int(line['timestamp'][11:13]) < 4) for line in json_data])
