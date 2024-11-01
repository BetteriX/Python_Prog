#!/usr/bin/env python3


def test(li: list):
    li.sort()

    fele_hossz = len(li) // 2
    if len(li) % 2 != 0:
        return li[fele_hossz]
    else:
        return (li[fele_hossz] + li[fele_hossz - 1]) / 2


def main():
    print(test([1, 2, 3, 4, 5]) == 3)
    print(test([3, 1, 2, 5, 3]) == 3)
    print(test([1, 300, 2, 200, 1]) == 2)
    print(test([3, 6, 20, 99, 10, 15]) == 12.5)


if __name__ == "__main__":
    main()
