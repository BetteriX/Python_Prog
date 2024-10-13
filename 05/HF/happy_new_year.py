def ev():
    elso = ord("z") - ord("H")
    masodik = ord("z") - ord("J")
    harmadik = ord("z") - ord("H")
    negyedik = ord("z") - ord("F")

    ev = chr(elso) + chr(masodik) + chr(harmadik) + chr(negyedik)
    return ev


def main():
    print(ev())


if __name__ == "__main__":
    main()
