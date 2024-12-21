#!/usr/bin/env python3


def my_func1(t: tuple):
    # return t[3]
    return t[-1]


def main():
    data = [
        (1, "Albany", "NY", 162692),
        (121, "Wyoming", "NY", 8722),
        (3, "Allegany", "NY", 11986),
        (123, "Yates", "NY", 5094),
    ]

    print("eredeti:\n", data)
    print("rendezetett:\n", sorted(data, key=my_func1))


if __name__ == "__main__":
    main()
