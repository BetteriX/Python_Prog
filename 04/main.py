#!/usr/bin/env python3


def main():
    # [24,...,32]
    # list(range(24,33))

    # [45,...,22]
    # list(range(45,21,-1))

    li = []
    # len(li) > 0:
    if li:
        print("nem üres")
    # len(li) == 0:
    if not li:
        print("üres")


if __name__ == "__main__":
    main()
