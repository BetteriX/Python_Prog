#!/usr/bin/env python3


class test:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return f"Az elem értéke: {self.data}"


def main():
    a = test(2)
    b = test(2)

    print(a == b)  # -> a.__eq__(b)


if __name__ == "__main__":
    main()
