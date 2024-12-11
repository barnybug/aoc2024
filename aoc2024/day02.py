from .utils import Answer


def is_safe(ns: list[int]) -> bool:
    diff = [a - b for a, b in zip(ns, ns[1:])]
    return all(1 <= d <= 3 for d in diff) or all(-3 <= d <= -1 for d in diff)


def is_safe2(ns: list[int]) -> bool:
    if is_safe(ns):
        return True
    for i in range(len(ns)):
        if is_safe(ns[:i] + ns[i + 1 :]):
            return True
    return False


def solve(input: str):
    numbers = [list(map(int, report.split())) for report in input.splitlines()]
    part1 = sum(is_safe(n) for n in numbers)
    part2 = sum(is_safe2(n) for n in numbers)
    return Answer(part1, part2)
