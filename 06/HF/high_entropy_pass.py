#!/usr/bin/env python3


def valid_passphrase(passphrase: str) -> bool:
    passphrase = passphrase.split()
    unique_words = set(passphrase)
    return len(passphrase) == len(unique_words)
    # for i in range(0, len(passphrase) - 1):
    #    for j in range(0, len(passphrase)):
    #        if i != j and passphrase[i] == passphrase[j]:
    #            return False
    # return True


def main():
    f = open("day04.txt", "r").readlines()

    valid_pass = 0
    for s in f:
        if valid_passphrase(s):
            valid_pass += 1

    print(valid_pass)


if __name__ == "__main__":
    main()
