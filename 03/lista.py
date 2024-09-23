#!/usr/bin/env python3

def product(numbers):
    total = 1
    for i in numbers:
        total *= i
    
    return total


def main():
    li = [2, 3, 6]
    result = product(li)
    print(result)


if __name__ == "__main__":
    main()