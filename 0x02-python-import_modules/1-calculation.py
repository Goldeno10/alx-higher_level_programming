#!/usr/bin/python3
from calculator_1 import add, mul, sub, div

a = 1
b = 2

if __name__ == "__main__":
    ad = add(a, b)
    print("{} + {} = {}".format(a, b, ad))
    su = sub(a, b)
    print("{} - {} = {}".format(a, b, su))
    mu = mul(a, b)
    print("{} * {} = {}".format(a, b, mu))
    di = div(a, b)
    print("{} / {} = {}".format(a, b, div))
