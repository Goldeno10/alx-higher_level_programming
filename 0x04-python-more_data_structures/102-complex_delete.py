#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in a_dictionary:
        if a_dictionary[i] == value:
            del a_dictionary[i]

#    a_dictionary = {k: v for k, v in a_dictionary.items() if v != value}
    return(a_dictionary)
