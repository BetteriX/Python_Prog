#!/usr/bin/env python3


def get_movie():
    return ("Total Recall", 1990, 7.5)


def main():
    """
    t = get_movie()
    title = t[0]
    year = t[1]
    score = t[2]
    """
    title, year, score = get_movie()
    print(title, year, score)


if __name__ == "__main__":
    main()
