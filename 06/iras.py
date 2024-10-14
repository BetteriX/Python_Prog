#!/usr/bin/env python3

import sys

INPUT = "szoveg.txt"
OUTPUT = "out.txt"


def main():
    f = open(INPUT, "r")
    w = open(OUTPUT, "w")

    for line in f:
        # line.rstrip("")
        w.write(line)

    w.close()
    f.close()

    # r - read    w - write    a - append
    # f = open("out.txt", "w")

    # print("hello", file=f)
    # print("world", file=f)

    # f.write("aa\n")
    # f.write("bb\n")

    # f.close()


if __name__ == "__main__":
    main()
