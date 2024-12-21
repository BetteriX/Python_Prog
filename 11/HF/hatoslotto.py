#!/usr/bin/env python3
# 6 szám összege => 90
# 6 szám szorzata => 996300


def osszeg(t: list[int]) -> int:
    return sum(t)


def szorzat(t: list[int]) -> int:
    result = 1
    for n in t:
        result *= n

    return result


def find_numbers() -> list[int]:
    target_osszeg = 90
    target_szorzat = 996300
    szamok = range(1, 46)

    for a in szamok:
        for b in szamok:
            # Azért hogy elkerüljük a duplikációkat azért tovább léptetjük az adott számot
            # Mert hogyha a b=1 és a=2 akkor azt addig lépteti tovább még nem lesz b=3
            if b <= a:
                continue
            for c in szamok:
                if c <= b:
                    continue
                for d in szamok:
                    if d <= c:
                        continue
                    for e in szamok:
                        if e <= d:
                            continue
                        for f in szamok:
                            if f <= e:
                                continue
                            talalt_szamok = [a, b, c, d, e, f]
                            if (
                                osszeg(talalt_szamok) == target_osszeg
                                and szorzat(talalt_szamok) == target_szorzat
                            ):
                                return talalt_szamok

    return []


def main():
    nyertes_szamok = find_numbers()
    if nyertes_szamok:
        print("A nyertes szamok:", nyertes_szamok)
    else:
        print("Nincs meg a nyertes szám!")


if __name__ == "__main__":
    main()
