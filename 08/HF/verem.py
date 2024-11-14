#!/usr/bin/env python3


class Verem:
    def __init__(self):
        self.data = []

    def ures(self):
        return len(self.data) == 0

    def betesz(self, num):
        self.data.append(num)

    def meret(self):
        return len(self.data)

    def kivesz(self):
        if not self.ures():
            return self.data.pop()
        else:
            return None

    def __str__(self):
        values = ""
        for d in self.data:
            values += str(d) + " "
        return f"[{values}"


def main():
    v = Verem()
    print(v)
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)


if __name__ == "__main__":
    main()
