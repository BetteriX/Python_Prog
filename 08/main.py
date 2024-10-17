#!/usr/bin/env python3


class EmptyClass:  # PascalCase
    pass


class MyClass:
    def hello(self):
        return "hello world"


def main():
    is_palindrom = True  # snake_case
    obj = EmptyClass()

    h = MyClass()
    print(h.hello())


if __name__ == "__main__":
    main()
