def print_rhombus(n: int):  # global namespace
    GROWING: int = 1  # local namespace
    SHRINKING: int = -1

    # fn in fn: it is called closure
    def print_line(i: int, direction: int):  # local namespace: visible in print_rhombus
        if i == 0:  # i is is part of the local namespace of print_line
            return
        line = ' ' * (n - i) + '* ' * i  # line is is part of the local namespace of print_line
        print(line.rstrip())
        if i == n:
            direction = SHRINKING  # change is happening in the local namespace of print_line
        print_line(i + direction, direction)  # recursion
    print_line(1, GROWING)


print_rhombus(int(input()))
