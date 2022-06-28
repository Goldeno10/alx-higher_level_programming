#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        check_3_mult = num % 3
        check_5_mult = num % 5
        if check_3_mult == 0:
            num = "Fizz"
        if check_5_mult == 0:
            num = "Buzz"
        if check_5_mult == 0 and check_3_mult == 0:
            num = "FizzBuzz"
        print("{}".format(num), end=" ")

