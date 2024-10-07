#!/usr/bin/env python3


def main():
    # 1.
    elems = ["auto", "villamos", "metro"]

    result = [s.upper() + "!" for s in elems]

    # 2.
    nevek = ["aladar", "bela", "cecil"]

    result = [s.capitalize() for s in nevek]

    # 3.
    zeroes = [0 for i in range(10)]

    # 4.
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    nums2 = [i for i in range(1, 11)]

    # result = [n + n for n in nums]

    result = list(range(2, 21, 2))

    # 5.
    elems = [str(i) for i in range(1, 11)]

    result = [int(i) for i in elems]

    # 6.
    s = "123456"

    result = [int(c) for c in s]

    # 7.
    s = "The quick brown fox jumps over the lazy dog"

    result = [len(sz) for sz in s.split()]


if __name__ == "__main__":
    main()
