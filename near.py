"""
Create a function that when given two strings of letters, determine whether the second can be made from the first by removing one 
letter. The remaining letters must stay in the same order.

Example

>>> near("reset", "rest")
True
>>> near("dragoon", "dragon")
True
>>> near("eave", "leave")
False
>>> near("sleet", "lets")
False
"""
# Start by making the simplest version of it so, a function that checks if two strings are identical
# Now you need to see if string 2 can be made from string 1
# Consider turning into a list to work with indexes?
# Consider using char to focus on breaking down to char and index position
# Research strings module for inspiration
# You need a way of checking to see if the string 2 can be made from string 1 - do x number of characters from 1 appear in 2...

def near(string1, string2):
    if string1 == string2:
        return "True"
    else:
        return "False"

print(near("reset", "reset"))