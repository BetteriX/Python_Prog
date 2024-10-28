#!/usr/bin/env python3

import sys


def main():
    szamsor = input("Adja meg a számsort: ")

    hossz = len(szamsor)
    if hossz % 4 != 0:
        print("Hibás számsor!")
        sys.exit(1)

    i = 0
    while i < hossz:
        negy_szamjegy = list(szamsor[i : i + 4])

        j = 0
        total = 0
        while j < 4:
            total += int(negy_szamjegy[j])
            j += 1

        print(str(total), end=" ")

        i += 4

    print()


if __name__ == "__main__":
    main()
