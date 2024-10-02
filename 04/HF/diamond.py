#!/usr/bin/env python3

import sys


def print_sor(space, csillag):
    print(" " * space + "*" * csillag + " " * space)


def main():
    magassag = int(input("Magasság: "))

    if magassag % 2 == 0:
        sys.exit("A magasságnak páratlannak kell lennie!")

    magassag_fele = magassag // 2
    space = magassag_fele
    csillag = 1

    for i in range(magassag_fele):
        print_sor(space, csillag)
        space -= 1
        csillag += 2

    for i in range(magassag_fele + 1):
        print_sor(space, csillag)
        space += 1
        csillag -= 2


if __name__ == "__main__":
    main()
