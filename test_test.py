from collections import defaultdict


def steam_leaf(data):
    stem_and_leaf = defaultdict(list)
    for numbers in data:
        first_dig = int(str(numbers)[:1])
        steam = int(str(numbers)[1::])
        if steam not in stem_and_leaf[first_dig]:
            stem_and_leaf[first_dig].append(steam)

    return stem_and_leaf


print(steam_leaf([11, 12, 12, 12, 21, 33]))
