#!/usr/bin/env python3

import json


def main():
    fname = "person.json"
    f = open(fname, "r")

    d = json.load(f)
    # d = json.loads(string) Egy sztringet olvas be

    f.close()

    print(type(d))
    print(d["daughter"]["age"])


if __name__ == "__main__":
    main()
