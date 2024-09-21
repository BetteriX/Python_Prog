#!/usr/bin/env python3

def szam_megfordit(number):
    return number[::-1]

def main():
    szam = input("Adjon meg egy egész számot: ")

    szam_megforditva = szam_megfordit(szam)
    print(szam_megforditva)

if __name__ == "__main__":
    main()