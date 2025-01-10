from collections import deque

from .utils import Answer, Point


def count(pos, lookup, part2=False):
    done = set()
    queue = deque([pos])
    score = 0
    while queue:
        pos = queue.popleft()
        n = lookup[pos]
        for p in (pos.up, pos.down, pos.left, pos.right):
            if p in done:
                continue
            if (o := lookup.get(p)) and o == n + 1:
                if not part2:
                    done.add(p)
                if o == 9:
                    score += 1
                else:
                    queue.append(p)

    return score


def s(c):
    if c == ".":
        return -1
    return int(c)


def solve(input: str):
    grid = input.splitlines()
    width, height = len(grid[0]), len(grid)
    lookup = {Point(x, y): s(grid[y][x]) for x in range(width) for y in range(height)}
    part1 = sum(count(p, lookup) for p, c in lookup.items() if c == 0)
    part2 = sum(count(p, lookup, True) for p, c in lookup.items() if c == 0)
    return Answer(part1, part2)
