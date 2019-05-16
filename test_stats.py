from collections import defaultdict


def steam_leaf(data):
    d = defaultdict(list)
    for numbers in data:
        first_dig = int(str(numbers)[:1])
        if numbers not in d:
            d[first_dig].append(int(str(numbers)[1::]))

    return d


print(steam_leaf([11, 12, 14, 23,32,24]))
