#!/usr/bin/env python3

from prim_utils import decimal_to_binary, palindrom_e


def main():
    total_sum = 0
    limit = 1_000_000
    for n in range(1, limit):
        if palindrom_e(str(n)):
            print(
                f"\rLoading: {(n) / (limit/100):.0f}%", end="", flush=True
            )  # Loading %
            binary = decimal_to_binary(n)
            if palindrom_e(binary):
                total_sum += n

    print("\n" + str(total_sum))


if __name__ == "__main__":
    main()
