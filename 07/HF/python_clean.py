#!/usr/bin/env python3


def main():
    f = open("string1.py", "r")
    w = open("string1_clean.py", "w")

    for line in f:
        line = line.rstrip("\n")
        if not line.lstrip().startswith("#"):
            print(line, file=w)

        # hashtag = line.find("#")
        # if hashtag == -1 and line.strip() != "":
        # if hashtag == -1:
        #    w.write(str(line))

    f.close()
    w.close()


if __name__ == "__main__":
    main()
