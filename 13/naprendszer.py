#!/usr/bin/env python3

import re


def main():
    f = open("DT2.csv", "r")

    for line in f:
        line = line.split(",")
        szoveg = line[0]

        m = re.search(r"j.*s.*u.*n", szoveg)
        if m:
            print(m.group())

    f.close()


if __name__ == "__main__":
    main()
