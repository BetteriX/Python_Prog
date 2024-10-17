#!/usr/bin/env python3

import json

import requests


def main():
    url = "https://jsonip.com/"

    r = requests.get(url)

    d = json.loads(r.text)
    print("Az ön ip címe: " + d["ip"])


if __name__ == "__main__":
    main()
