#!/usr/bin/env python3


def sorrend_ellenoriz(szoveg):
    return all(letter in szoveg for letter in ["j", "s", "u", "n"])


def main():
    f = open("DT2.csv", "r")
    szavak = []

    for line in f:
        line = line.split(",")
        szoveg = line[0]

        if sorrend_ellenoriz(szoveg):
            szavak.append(szoveg)

    f.close()

    print(szavak)


if __name__ == "__main__":
    main()
