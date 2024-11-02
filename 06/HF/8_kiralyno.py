#!/usr/bin/env python3


def sor_kirajzol(num):
    result = "|"

    for i in range(0, 8):
        result += " "
        if i == num:
            result += "Q"
        else:
            result += "."

    result += " |"
    return result


def sakk_tabla_kirajzol(li: list):
    print("+-----------------+")
    sor = 7
    while sor >= 0:
        index = 0
        for i in range(0, 8):
            if li[i] == sor:
                index = i
                break

        sor -= 1
        print(sor_kirajzol(index))

    print("+-----------------+")


def main():
    sakk_tabla_kirajzol([0, 4, 7, 5, 2, 6, 1, 3])


if __name__ == "__main__":
    main()
