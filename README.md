# Python Assignment 1
### Assignment: Bob Ross Twitch Chatlog 2015 - https://github.com/HawkDon/Python_Assignment1

## Group 
**Foolish Supermarket** - Alexander (cph-ah353), Stanislav (cph-sn186), Mathias B. (cph-mb493), Mikkel L. (cph-ml474)



## Project Deescription
This is a program written to interact with a specific dataset (see example below). 

When the program receives the URL to the data as input, it downloads the file, cleans-up/manipulates the input data and computes certain statistics.

(The statistics are related to the list of tasks specified in the assignment description [here](https://github.com/datsoftlyngby/dat4sem2018fall-python/blob/master/assignments/assignment1.md)).


## Dependencies

This project uses the Requests library. To install Requests, write (in your terminal of choice):

``` pip install requests ```

## How to run (from CLI)

In root of folder, in your terminal of choice, write: 

``` python main.py <url> <filename>[optional] ```

example:

```python main.py https://raw.githubusercontent.com/HawkDon/Python_Assignment1/master/BobRoss.txt```

## Results

- How many lines does the .txt file have? =  181533
- How many times does the .txt file write "RUINED" ? =  5477
- How many messages was written after 05:00pm ? =  180513
- How many different users does the .txt file contain ? =  67568
- What is most used word in the .txt file ? =  ('KappaRoss', 36068)

