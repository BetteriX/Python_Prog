#!/usr/bin/env python3


def get_nyomtando(input: str) -> str:
    oldalak = input.split(",")

    nyomtando = []
    for n in oldalak:
        if "-" in n:
            # n = n.split("-")
            start, end = n.split("-")
            for i in range(int(start), int(end) + 1):
                nyomtando.append(i)
        else:
            nyomtando.append(int(n))

    nyomtando = ",".join(str(num) for num in nyomtando)
    return nyomtando
