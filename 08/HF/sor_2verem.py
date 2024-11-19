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
        # values = ""
        # for d in self.data:
        #    values += str(d) + " "

        values = " ".join(str(d) for d in self.data)
        return f"[{values}"


class MyQueue:
    def __init__(self):
        self.verem1 = Verem()
        self.verem2 = Verem()

    def append(self, num):
        self.verem1.betesz(num)

    def popleft(self):
        if self.verem2.ures():
            while not self.verem1.ures():
                self.verem2.betesz(self.verem1.kivesz())

        if not self.verem2.ures():
            return self.verem2.kivesz()
        else:
            return None

    def is_empty(self):
        return self.verem1.ures() and self.verem2.ures()

    def size(self):
        return self.verem1.meret + self.verem2.meret


def main():
    pass


if __name__ == "__main__":
    main()
