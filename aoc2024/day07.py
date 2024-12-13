import numpy as np

from .utils import Answer, split_numbers


def valid(line: str, part2: bool):
    test, a = line.split(": ")
    test = int(test)
    vs = split_numbers(a, " ")
    accs = np.array(vs[:1])
    for v in vs[1:]:
        additions = accs + v
        products = accs * v
        if part2:
            concats = accs * (10 ** len(str(v))) + v
            accs = np.concat([additions, products, concats])
        else:
            accs = np.concat([additions, products])

    if test in accs:
        return test
    return 0


def solve(input: str):
    part1 = sum(valid(line, False) for line in input.splitlines())
    part2 = sum(valid(line, True) for line in input.splitlines())
    return Answer(part1, part2)
