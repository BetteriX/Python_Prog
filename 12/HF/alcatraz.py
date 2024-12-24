#!/usr/bin/env python3


def zar(li: list[bool], start: int, freq: int) -> list[bool]:
    for i in range(start, len(li), freq):
        if li[i]:
            li[i] = False
        else:
            li[i] = True


def zar_nyitva(li: list[bool]) -> str:
    result = [str(i) for i in range(1, len(li)) if li[i]]
    return "".join(result)


def main():
    # inicializálás 1-601-ig
    cellak = [False] * 601  # A 0. index-t nem használjuk

    for lepes in range(1, len(cellak)):
        zar(cellak, lepes, lepes)

    print(zar_nyitva(cellak))


if __name__ == "__main__":
    main()
