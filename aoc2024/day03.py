import re

from .utils import Answer


def solve(input: str):
    part1 = 0
    part2 = 0
    for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", input):
        a, b = map(int, m.groups())
        part1 += a * b

    enabled = True
    for m in re.finditer(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)", input):
        s = m.group().split("(")[0]
        if s == "do":
            enabled = True
        elif s == "don't":
            enabled = False
        elif enabled:
            a, b = map(int, m.groups())
            part2 += a * b
    return Answer(part1, part2)
