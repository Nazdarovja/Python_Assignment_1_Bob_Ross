from Utility.Textfile2json import convert
import number_of_ruined as nor
import after_5pm as a5
from most_used_word import find_most_used_word as most_used_word

def create_statistics(text_file):
    """Takes -txt file as input. Prints statistics."""
    json_data = convert(text_file)

    num_of_lines = len(json_data)
    num_of_ruined = nor.get_number_of_ruined(json_data)
    num_of_after_5 = a5.after_5pm(json_data)

    print("How many lines does the .txt file have? = ", num_of_lines)
    print("How many times does the .txt file write \"RUINED\" ? = ",  num_of_ruined)
    print("How many messages was written after 05:00 ? = ", num_of_after_5)
    print("How many different users does the .txt file contain ? = ")
    print("What is most used word in the .txt file ? = ")
