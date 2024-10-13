#!/usr/bin/env python3

import os
import sys


def main():
    name = sys.argv[0]

    if "z-a.py" in name:
        print("".join([chr(i) for i in range(ord("z"), ord("a") - 1, -1)]))
    else:
        print("".join([chr(i) for i in range(ord("a"), ord("z") + 1)]))


if __name__ == "__main__":
    main()
