#!/usr/bin/env python3

import nyomtando


def main():
    oldalak = input("Nyomtandó oldalak: ")

    output = nyomtando.get_nyomtando(oldalak)
    print(output)


if __name__ == "__main__":
    main()
