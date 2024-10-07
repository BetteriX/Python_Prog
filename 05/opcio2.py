#!/usr/bin/env python3


def loop(amount, debug=False):
    if debug:
        print("# start loop")

    for i in range(1, amount + 1):
        print(i)

    if debug:
        print("# end loop")


def main():
    loop(5, debug=True)


if __name__ == "__main__":
    main()
