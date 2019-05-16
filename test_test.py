from collections import defaultdict
class dictdict():
    pass


def steam_leaf(data):
    stem_and_leaf = defaultdict(list)
    for numbers in data:
        stem = int(str(numbers)[:1])
        leaf = int(str(numbers)[1::])
        if leaf not in stem_and_leaf[stem]:
            stem_and_leaf[stem].append(leaf)

    return stem_and_leaf


print(steam_leaf([11, 12, 12, 12, 21, 33]))
