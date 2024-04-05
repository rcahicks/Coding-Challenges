# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry about strings with less than two characters.

def remove_char(s):
    s_list = list(s)
    s_list.pop(0)
    s_list.pop(len(s_list) - 1)
    return ''.join(s_list)