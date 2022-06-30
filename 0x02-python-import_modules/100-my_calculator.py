if __name__ == "__main__":
    import calculator_1 as calc
    import sys

    arg_c = len(sys.argv) - 1
    arg_v = sys.argv

    if arg_c != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(arg_v[1])
    b = int(arg_v[3])
    op = arg_v[2]
    if op == "+":
        c = cal.add(a, b)
        print("{} {} {} = {}".format(a, op, b, c))
    elif op == "-":
        c = calc.sub(a, b)
        print("{} {} {} = {}".format(a, op, b, c))
    elif op == "*":
        c = calc.mul(a, b)
        print("{} {} {} = {}".format(a, op, b, c))
    elif op == "/":
        c = calc.div(a, b)
        print("{} {} {} = {}".format(a, op, b, c))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
