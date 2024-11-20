#!/usr/bin/env python3


def main():
    f = open("input.txt", "r")

    sum = 0
    for nums in f.readlines():
        nums = nums.strip()

        min, max = float("inf"), float("-inf")
        # for num in nums.split(" ") teszt.txt
        for num in nums.split("\t"):  # day02.txt
            int_num = int(num)

            if int_num < min:
                min = int_num

            if int_num > max:
                max = int_num

        sum += max - min

    print(sum)


if __name__ == "__main__":
    main()
