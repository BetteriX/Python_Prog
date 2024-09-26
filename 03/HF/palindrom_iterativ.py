#!/usr/bin/env python3


def palindrom_e(szo):
    max = len(szo) - 1
    min = 0
    while min <= max:
        if szo[max] != szo[min]:
            return True
        max -= 1
        min += 1

    return False


def main():
    egy_szo = "görögg"

    print(palindrom_e(egy_szo))


if __name__ == "__main__":
    main()
