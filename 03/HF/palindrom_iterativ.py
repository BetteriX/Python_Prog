#!/usr/bin/env python3


def palindrom_e(szo):
    max = len(szo) - 1
    min = 0
    while min <= max:
        if szo[max] != szo[min]:
            return False
        max -= 1
        min += 1

    return True


def main():
    egy_szo = "görög"

    print(palindrom_e(egy_szo))


if __name__ == "__main__":
    main()
