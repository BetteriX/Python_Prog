#!/usr/bin/env python3

import sys

def hello(s):
    print("Hello " + s + "!")

def main():
    # print("Hello " + sys.argv[1] + "!")
    name = sys.argv[1]
    hello(name)


if __name__ == "__main__":
    main()