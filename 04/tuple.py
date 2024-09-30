#!/usr/bin/env python3


def main():
    x, y = (3, 5)

    print("Elötte: ")
    print(x, y)

    # tmp = x
    # x = y
    # y = tmp

    # Így is lehet
    x, y = y, x

    print("Utána: ")
    print(x, y)


if __name__ == "__main__":
    main()
