#!/usr/bin/env python3


class Sor:
    def __init__(self):
        self.data = []

    def enqueue(self, num):
        self.data.append(num)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None

    def peek(self):
        return self.data[0]

    def count(self):
        return len(self.data)

    def clear(self):
        self.data.clear()

    def __str__(self):
        # values = ""
        # for d in self.data:
        #    values += str(d) + " "

        values = " ".join(str(d) for d in self.data)
        return f"[{values}]"


def main():
    s = Sor()
    s.enqueue(4)
    s.enqueue(1)
    s.enqueue(3)
    print(s)
    x = s.dequeue()
    print(s)
    sor_eleje = s.peek()
    print(sor_eleje)
    print(s.count())
    print(s)

    s.clear()
    print(s.count())


if __name__ == "__main__":
    main()
