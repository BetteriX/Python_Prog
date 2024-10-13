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


def find_munchausen_numbers(limit):
    digits = [0, 0, 0, 0]
    munchausen_numbers = []

    while True:
        first_digit, second_digit, third_digit, forth_digit = digits

        sum_of_powers = (
            (forth_digit**forth_digit if forth_digit != 0 else 0)
            + (third_digit**third_digit if third_digit != 0 else 0)
            + (second_digit**second_digit if second_digit != 0 else 0)
            + (first_digit**first_digit if first_digit != 0 else 0)
        )

        number = (
            forth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit
        )

        if number >= limit:
            break

        if sum_of_powers == number:
            print(number)
            munchausen_numbers.append(number)

        digits = increment_digit(digits)

    return munchausen_numbers


def main():
    print("Összes Münchausen szám 10,000-ig: ")
    print(find_munchausen_numbers(10000))

    print("Összes Münchausen szám 440,000,000-ig: ")
    print(find_munchausen_numbers(440_000_000))


if __name__ == "__main__":
    main()
