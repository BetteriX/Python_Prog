#!/usr/bin/env python3


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"


def main():
    rect = Rectangle(50, 10)
    rect.width = 60
    # print(rect.area())

    print(rect)


if __name__ == "__main__":
    main()
