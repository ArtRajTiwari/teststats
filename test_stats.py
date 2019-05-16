import math


def steam_leaf(array_of_dat):
    d = []
    for num in array_of_dat:
        def first_n_digits(num, n=1):
            return num // 10 ** (int(math.log(num, 10)) - n + 1)

        first_digit = first_n_digits(num)
        print(str(d))

        if num in range(0,20):
            d.append(num)

    return d


print(steam_leaf([15, 23, 34, 23, 11, 10, 12, 14, 30, 32]))
# steam_leaf([21,22,12,13,14])
