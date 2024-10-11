#!/usr/bin/env python3

import os
import sys


def main():
    parts = []
    for i in range(1, 15 + 1):
        parts.append(str(i))
    res = parts.join("")


if __name__ == "__main__":
    main()
