def after_5pm(json_data):
    """Takes list of json as input. Returns number chat messages after 17/5pm

        Args: 
            json_data: List of Dictionaries.

        Returns: 
            int, num of chat messages.
    """

    # Dataset is limited to timestamps for <1 day, so possible to sort by hour >=17 or <4 o'clock. 
    return len([(int(line['timestamp'][11:13]) >= 17 or int(line['timestamp'][11:13]) < 4) for line in json_data])
