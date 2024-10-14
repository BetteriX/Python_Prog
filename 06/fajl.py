#!/usr/bin/env python3


def main():
    # r - read    w - write    a - append
    f = open("szoveg.txt", "r")

    # for line in f:
    # if line.endswith(".\n"):
    #    print(line, end="")

    # line = line.rstrip("\n")
    # if line.endswith("."):
    #    print(line)

    # sorok = f.readlines()
    # print(sorok)

    # content = f.read()
    # print("'" + content + "'")

    sorok = f.read().splitlines()
    print(sorok)

    f.close()


if __name__ == "__main__":
    main()
