from collections import Counter

from .utils import Answer


def solve(input: str):
    lines = [line.split() for line in input.strip().split("\n")]
    list1 = [int(l[0]) for l in lines]
    list2 = [int(l[1]) for l in lines]
    list1.sort()
    list2.sort()

    counts = Counter(list2)

    part1 = sum(abs(a - b) for a, b in zip(list1, list2))
    part2 = sum(a * counts[a] for a in list1)
    return Answer(part1, part2)
