#!/usr/bin/env python3

import sys


def cat(fname: str):
    try:
        f = open(fname)

        print("---", fname)
        for line in f:
            print(line, end="")

        f.close()
    except FileNotFoundError as e:
        print("--- I/O Error:", e)


def main():
    args = sys.argv[1:]

    for arg in args:
        cat(arg)


if __name__ == "__main__":
    main()
