#!/usr/bin/env python3


def main():
    f = open("string1.py", "r")
    w = open("string1_clean.py", "w")

    for line in f:
        hash = line.find("#")
        if hash == -1:
            w.write(str(line))

    f.close()
    w.close()


if __name__ == "__main__":
    main()