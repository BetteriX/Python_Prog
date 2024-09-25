#!/usr/bin/env python3


def szamok_szorzata(lista):
    szorzat = 1

    for n in lista:
        szorzat *= n

    return szorzat


def main():
    szamok = [3, 5, 7, 9]

    szorzat = szamok_szorzata(szamok)

    print(szorzat)


if __name__ == "__main__":
    main()
