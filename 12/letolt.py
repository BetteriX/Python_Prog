#!/usr/bin/env python3

import urllib.request

from pygyak import get_page


def main():
    url = "https://www.python.org/"
    # response = urllib.request.urlopen(url)

    # raw = response.read()
    # print(type(raw))
    # print(raw)

    # html = raw.decode("utf-8")
    # print(type(html))
    # print(html)raw

    print(get_page(url))


if __name__ == "__main__":
    main()
