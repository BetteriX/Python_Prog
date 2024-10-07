#!/usr/bin/env python3


# def greet(name, greetings="Hello"):
#    print(f"{greetings} {name}!")


def greet(name, repeat=1, postfix=""):
    for i in range(repeat):
        print(name + postfix)


def main():
    # greet("Zsolt")
    # greet("Zsolt", greetings="Hola")

    greet("Anna", repeat=2, postfix="!")


if __name__ == "__main__":
    main()
