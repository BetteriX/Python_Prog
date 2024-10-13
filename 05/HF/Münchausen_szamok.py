#!/usr/bin/env python3


def increment_digit(digits):
    first, second, third, forth = digits

    if first == 9:
        first = 0
        if second == 9:
            second = 0
            if third == 9:
                third = 0
                forth += 1
            else:
                third += 1
        else:
            second += 1
    else:
        first += 1

    return first, second, third, forth


def Muchausen():
    digits = [0, 0, 0, 0]
    much_numbers = []

    while True:
        first_digit, second_digit, third_digit, forth_digit = digits

        num = (
            (forth_digit**forth_digit if forth_digit != 0 else 0)
            + (third_digit**third_digit if third_digit != 0 else 0)
            + (second_digit**second_digit if second_digit != 0 else 0)
            + (first_digit**first_digit if first_digit != 0 else 0)
        )

        ev = forth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit

        if ev >= 10000:
            break

        if num == ev:
            print(num)
            much_numbers.append(ev)

        digits = increment_digit(digits)

    return much_numbers


def main():
    print("Összes Muchausen szám: ")
    print(Muchausen())


if __name__ == "__main__":
    main()
