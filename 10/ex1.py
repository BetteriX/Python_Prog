#!/usr/bin/env python3

# import pygyak as pgy
from pygyak import is_prime


def main():
    print("100-nál kisebb primszámok: ")
    for i in range(2, 100):
        if is_prime(i):
            print(i, end=" ")

    print()


if __name__ == "__main__":
    main()
