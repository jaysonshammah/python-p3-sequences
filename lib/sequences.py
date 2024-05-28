#!/usr/bin/env python3

def print_fibonacci(length):
    pass

    if length <= 0 or len(str(length)) == 0:
        print([])
        return

    result = []
    a, b = 0, 1
    for i in range(length):
        result.append(a)
        a, b = b, b+a

    print(result)

print_fibonacci(0)