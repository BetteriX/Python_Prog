#!/usr/bin/env python3


def sorrend_ellenoriz(szoveg):
    szavak = ["j", "s", "u", "n"]
    i = 0
    for c in szoveg:
        if c == szavak[i]:
            i += 1

    if i == 4:
        return True
    return False


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
