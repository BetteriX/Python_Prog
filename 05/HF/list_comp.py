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

    # 8.
    s = "python is an awesome language"

    result = [sz[0] for sz in s.split()]

    # 9.
    s = "The quick brown fox jumps over the lazy dog"

    result = [(sz, len(sz)) for sz in s.split()]

    # 10.
    result = [i for i in range(0, 10, 2)]

    # 11.
    result = [i * i for i in range(0, 20, 2)]

    # 12.
    result = [i * i for i in range(20) if str(i * i).endswith("4")]

    # 13.
    s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    result = "".join(s)

    # 14.
    s = [" apple ", " banana ", " kiwi "]

    result = [word.replace(" ", "") for word in s]

    # 15.
    list = [1, 0, 1, 1, 0, 1, 0, 0]

    result = "".join(str(num) for num in list)
    print(result)


if __name__ == "__main__":
    main()
