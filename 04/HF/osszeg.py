#!/usr/bin/env python3


def main():
    negyzet_osszege = 0
    osszeg_negyzete = 0
    for i in range(1, 100 + 1):
        negyzet_osszege += i * i
        osszeg_negyzete += i

    osszeg_negyzete *= osszeg_negyzete

    result = osszeg_negyzete - negyzet_osszege

    print(result)


if __name__ == "__main__":
    main()
