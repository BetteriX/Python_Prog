#!/usr/bin/env python3


def clear_whitespace(szoveg):
    return [s.replace("\n", "").replace(" ", "") for s in szoveg]


def main():
    szoveg = ["192.20.246.138:\n 6666", "206.130.99.82:\n8080"]

    print("Előtte:\n" + str(szoveg))

    szetvalasztott_szoveg = clear_whitespace(szoveg)
    print("Utána:\n" + str(szetvalasztott_szoveg))


if __name__ == "__main__":
    main()
