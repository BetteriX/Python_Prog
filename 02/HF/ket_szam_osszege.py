#!/usr/bin/env python3

import sys

def main():
    if(len(sys.argv) == 3):
        szam1 = int(sys.argv[1])
        szam2 = int(sys.argv[2])
        sum = szam1+szam2
        print("A két szám összege: " + str(sum))
    else:
        print("Az argumentumba csak 2 db szám lehet!")

if __name__ == "__main__":
    main()