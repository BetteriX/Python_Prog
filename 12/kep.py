#!/usr/bin/env python3

import urllib.request


def main():
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"

    urllib.request.urlretrieve(url, "logo.png")
    print("END")


if __name__ == "__main__":
    main()
