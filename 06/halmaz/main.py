#!/usr/bin/env python3


def main():
    a = ["alma", "banan", "citrom"]

    a = set(a)
    b = set()

    b.add("banan")
    b.add("narancs")

    print(a.union(b))
    print(a.intersection(b))
    print(a.difference(b))

    is_kiwi = "kiwi" in a  # Ez egy nagyon gyors, hashinget használ


if __name__ == "__main__":
    main()
