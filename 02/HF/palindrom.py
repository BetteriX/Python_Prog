#!/usr/bin/env python3

def palindrom_e(s):
    s_megfordit = s[::-1]

    if(s == s_megfordit):
        return 1
    else:
        return 0

def main():
    s = input("Adj meg egy szöveget: ")

    palindrom = palindrom_e(s)

    if(palindrom == 1):
        print("A szöveg palindrom!")
    else:
        print("A szöveg nem palindrom!")

if __name__ == "__main__":
    main()