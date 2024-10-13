#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    valid_char = ""

    for t in text:
        for c in chars:
            if t == c:
                valid_char += t

    return valid_char


def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()
