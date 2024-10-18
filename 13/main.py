#!/usr/bin/env python3

import re


def Find(pat, text):
    m = re.search(pat, text)
    if m:
        print(m.group())
    else:
        print("nincs benne")


def main():
    Find("fej", "regularis kifejezesek")

    Find("unix", "regularis kifejezesek")

    Find("f.j", "regularis kifejezesek")
    Find("f.j", "fojtas")

    m = re.search(r"([\w.]+)@([\w.]+)", "vmi szabozsolt430@gmail.com END")

    print(m.group(0))
    print(m.group(1))

    m = re.findall(
        r"([\w.]+)@([\w.]+)", "vmi szabozsolt430@gmail.com END valami@gmail.com"
    )

    print(m)

    s = "vmi zsolt@gmail.com         vmi        valami@hotmail.com     END"

    print(re.sub(r"([\w.]+)@[\w.]+", r"\1@tatooine.com", s))


if __name__ == "__main__":
    main()
