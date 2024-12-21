#!/usr/bin/env python3


def sort(m):
    return m[1]


def main():
    matrix = [[2, 6], [1, 3], [5, 4]]

    print("eredeti:\n", matrix)
    print("rendezetett:\n", sorted(matrix, key=sort))


if __name__ == "__main__":
    main()
