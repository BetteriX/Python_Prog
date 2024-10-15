#!/usr/bin/env python3
import pygyak


def main():
    total = 0
    # for i in range(0, 200):
    #    if pygyak.is_prime(i):
    #        total += i

    total = sum([i for i in range(2, 200) if pygyak.is_prime(i)])

    print("200-nál kisebb primszámok összege: " + str(total))


if __name__ == "__main__":
    main()
