#!/usr/bin/env python3

INPUT = "szamok.txt"


def main():
    # f = open(INPUT, "r")

    # total = 0
    # for line in f:
    #    # line = line.strip()
    #    total += int(line)

    # f.close()

    total = 0
    with open(INPUT, "r") as f:
        for line in f:
            # line = line.strip()
            total += int(line)

    print(str(total)[:10])


if __name__ == "__main__":
    main()
