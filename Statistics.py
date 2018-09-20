from Utility.Textfile2json import convert

def create_statistics(text_file):
    """Takes -txt file as input. Prints statistics."""
    json_data = convert(text_file)

    num_of_lines = len(json_data)
    # etc

    print("How many lines does the .txt file have? = ", num_of_lines)
    print("How many times does the .txt file write \"RUINED\" ? = ")
    print("How many messages was written after 05:00 ? = ")
    print("How many different users does the .txt file contain ? = ")
    print("What is most used word in the .txt file ? = ")
