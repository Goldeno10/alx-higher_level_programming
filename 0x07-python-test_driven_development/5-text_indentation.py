#!/usr/bin/python3
"""

"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    text_l = list(text)
    flag = 0;
    for i in text_l:
        if i not in [".", "?",":"] and flag == 0:
            print(f"{i}", end="")
            
        elif i not in [".", "?",":"] and flag == 1:
            if i == " ":
                continue
            else:
                print(f"{i}", end="")
                flag = 0
        else:
            print(f"{i}\n")
            flag = 1
