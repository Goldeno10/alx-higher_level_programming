#!/usr/bin/python3
def roman_to_int(roman_string):
    rmn = {"I": 1, "V": 5, "X": 10,
           "L": 50, "C": 100,
           "D": 500, "M": 1000}
    keys = list(rmn)
    Lst = list(roman_string)

    if roman_string is None:
        return 0
    for i in Lst:
        if i not in keys:
            return 0

    n_L = list(map(lambda x: rmn[x], Lst))
    for i in range(len(n_L)):
        if i > 0:
            if n_L[i] > n_L[i-1]:
                if i+1:
                    n_L[i-1:i+1] = [n_L[i] - n_L[i-1]]
                    n_L.append(0)
                else:
                    n_L[i-1:] = [n_L[i] - n_L[i-1]]
    return sum(n_L)
