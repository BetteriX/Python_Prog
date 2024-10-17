#!/usr/bin/env python3

import os


def main():
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"

    cmd = f"wget '{url}' -O python.png"
    print(cmd)
    os.system(cmd)


if __name__ == "__main__":
    main()
