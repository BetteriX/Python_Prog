#!/usr/bin/env python3


def main():
    szam = 2**1000

    total = 0
    for c in str(szam):
        total += int(c)

    print(total)


if __name__ == "__main__":
    main()
