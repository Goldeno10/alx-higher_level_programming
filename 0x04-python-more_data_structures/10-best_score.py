#!/usr/bun/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = 0
    key = None
    for k, v in a_dictionary.items():
        if v > score:
            score = v
            key = k
    return key
