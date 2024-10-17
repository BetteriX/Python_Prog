#!/usr/bin/env python3

import requests


def main():
    url = "https://index.hu"

    r = requests.get(url)
    print(r.text)


if __name__ == "__main__":
    main()
