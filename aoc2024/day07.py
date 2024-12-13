from .utils import Answer, split_numbers


def valid(line: str, part2: bool):
    test, a = line.split(": ")
    test = int(test)
    vs = split_numbers(a, " ")
    accs = [vs[0]]
    for v in vs[1:]:
        additions = [a + v for a in accs]
        products = [a * v for a in accs]
        accs = (
            additions
            + products
            + ([a * 10 ** len(str(v)) + v for a in accs] if part2 else [])
        )
        accs = [a for a in accs if a <= test]

    if test in accs:
        return test
    return 0


def solve(input: str):
    part1 = sum(valid(line, False) for line in input.splitlines())
    part2 = sum(valid(line, True) for line in input.splitlines())
    return Answer(part1, part2)
