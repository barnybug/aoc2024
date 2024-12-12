from functools import cmp_to_key

from .utils import Answer, split_numbers


def valid(update: list[int], rules: set):
    for i, a in enumerate(update):
        rest = update[i + 1 :]
        if any((a, b) not in rules for b in rest):
            return 0
    return update[len(update) // 2]


def solve(input: str):
    rules, updates = input.split("\n\n")
    rules = {tuple(split_numbers(rule, "|")) for rule in rules.splitlines()}
    part1, part2 = 0, 0
    for update in updates.splitlines():
        update = split_numbers(update)
        if n := valid(update, rules):
            part1 += n
        else:
            update.sort(key=cmp_to_key(lambda a, b: -1 if (a, b) in rules else 1))
            part2 += valid(update, rules)
    return Answer(part1, part2)
