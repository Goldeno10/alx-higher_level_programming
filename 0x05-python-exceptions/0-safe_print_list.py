
#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    n = x
    for i in range(x):
        try:
            print(my_list[i], end="")
            j += 1
        except:
            pass
    print()
    return (j)
