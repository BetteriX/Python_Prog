#!/usr/bin/env python3

import random


# Egy másolatott létrehozunk mert helyben modósitja a listát
def shuffled(li: list) -> list:
    li_copy = li[:]
    random.shuffle(li_copy)
    return li_copy


def main():
    li = [4, 3, 5, 7]

    print(shuffled(li)[-1])


if __name__ == "__main__":
    main()
