#!/usr/bin/env python3

MAX = 100

import sys

def hello(name, color, what):
    #v1
    #print("{0}, {1} az {2}! Ki? {0}".format(name, color, what))
    
    #v2 #Hibás
    #print("{}, {} az {}! Ki? {}".format(name, color, what))
    
    #v3
    print("{n}, {c} az {w}!".format(n=name.capitalize(), c=color, w=what))
    
    #v4
    #print(f"{name}, {color} az {what}!")

def main():
    #hello("geza", "kek", "eg")
    #print("-" * 40)

    s = "geza"
    print(s[-2:])

if __name__ == "__main__":
    main()