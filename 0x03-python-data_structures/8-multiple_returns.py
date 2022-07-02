#!/usr/bin/python3
def multiple_returns(sentence):
    _len = len(sentence)
    if _len < 1:
        return(_len, None)
    return (_len, sentence[0])
