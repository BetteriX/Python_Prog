#!/usr/bin/env python3

MELY_MGHK = "aáoóuú"
MAGAS_MGHK = "eéiíöőüű"


def hangrend(word):
    """
    hossz = len(word)
    i = 0
    while i < hossz:
        for mely in MELY_MGHK:
            if word[i] == mely:
                mely_van = 1

        for magas in MAGAS_MGHK:
            if word[i] == magas:
                magas_van = 1

        if mely_van and magas_van:
            return "vegyes"

        i += 1
    """

    mely_van = magas_van = False

    for char in word:
        if char in MELY_MGHK:
            mely_van = True
        elif char in MAGAS_MGHK:
            magas_van = True

        if mely_van and magas_van:
            return "vegyes"

    if mely_van:
        return "mély"
    elif magas_van:
        return "magas"
    else:
        return "semmilyen"


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]

    for i in words:
        print(i + " -> " + hangrend(i))


if __name__ == "__main__":
    main()
