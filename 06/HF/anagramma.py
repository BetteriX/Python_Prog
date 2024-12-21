#!/usr/bin/env python3


def normalize(word: str) -> str:
    return word.lower().replace(" ", "")


def main():
    s1 = "Clint Eastwood"
    s2 = "Old west action"

    s1 = normalize(s1)
    s2 = normalize(s2)

    print(s1)
    print(s2)


if __name__ == "__main__":
    main()
