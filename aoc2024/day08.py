from itertools import combinations

from .utils import Answer, Point


def solve(input: str):
    grid = input.splitlines()
    nodes = {
        Point(x, y): c
        for y, line in enumerate(grid)
        for x, c in enumerate(line)
        if c != "."
    }
    node_types = set(nodes.values())
    width, height = len(grid[0]), len(grid)

    part1 = set()
    part2 = set()
    for node_type in node_types:
        nnodes = [p for p, t in nodes.items() if t == node_type]
        for a, b in combinations(nnodes, 2):
            m = max(width, height)
            for i in range(-m, m):
                an = a + (a - b) * i
                if 0 <= an.x < width and 0 <= an.y < height:
                    if i in (1, -2):
                        part1.add(an)
                    part2.add(an)

    return Answer(len(part1), len(part2))
