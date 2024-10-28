#!/usr/bin/env python3

import sys


def main():
    f = open("szavak.txt")

    szavak = f.readlines()

    i = 0
    while i < len(szavak):
        elso_szo = szavak[i].strip()[-3:]
        j = i + 1
        while j < len(szavak):
            masodik_szo = szavak[j].strip()[-3:]

            if elso_szo == masodik_szo:
                print(szavak[i].strip() + " - " + szavak[j].strip())
                sys.exit(0)
            j += 1

        i += 1

    f.close()


if __name__ == "__main__":
    main()
