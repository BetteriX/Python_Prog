#!/usr/bin/env python3

def main():
    szam = input("Adjon meg egy számot: ")

    print("Formázás nélkül: " + str(szam))
    print("Formázással: {0:,}".format(int(szam)))

if __name__ == "__main__":
    main()