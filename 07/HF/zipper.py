#!/usr/bin/env python3


def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord("a"), ord("z") + 1))

    for t in zip(codes, chars):
        print(t)


if __name__ == "__main__":
    main()
