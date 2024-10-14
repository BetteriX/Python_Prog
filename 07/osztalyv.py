#!/usr/bin/env python3


class Proba:
    # i = 12345
    counter = 0  # Osztályváltozó

    def __init__(self):
        Proba.counter += 1


def main():
    # print(Proba.i)

    print(Proba.counter)
    p1 = Proba()
    p2 = Proba()
    p3 = Proba()
    print(Proba.counter)


if __name__ == "__main__":
    main()
