#!/usr/bin/env python3

import json
import urllib


def main():
    url = "https://jsonip.com/"
    response = urllib.request.urlopen(url)

    web = response.read()
    decode = web.decode("utf-8")

    d = json.loads(decode)

    print("Az ön ip címe: " + d["ip"])


if __name__ == "__main__":
    main()
