#!/usr/bin/env python3


def main():
    osszeg = sum([i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0])

    print(osszeg)


if __name__ == "__main__":
    main()
