#!/usr/bin/env python3


def palindrom_e(szo):
    if len(szo) <= 1:
        return True

    return szo[0] == szo[-1] and palindrom_e(szo[1:-1])


def main():
    egy_szo = "lehel"

    print(palindrom_e(egy_szo))


if __name__ == "__main__":
    main()
