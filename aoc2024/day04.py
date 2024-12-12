from collections import defaultdict

from .utils import Answer


def solve(input: str):
    lines = input.splitlines()
    width, height = len(lines[0]), len(lines)
    grid = {(x, y): lines[y][x] for y in range(height) for x in range(width)}
    grid = defaultdict(lambda: ".", grid)

    part1, part2 = 0, 0
    for y in range(0, height):
        for x in range(0, width):
            dirs = [
                "".join(grid[x + i, y] for i in range(4)),
                "".join(grid[x, y + i] for i in range(4)),
                "".join(grid[x + i, y + i] for i in range(4)),
                "".join(grid[x - i, y + i] for i in range(4)),
            ]
            part1 += sum(s in ("XMAS", "SAMX") for s in dirs)
            corners = "".join(
                [grid[x, y], grid[x + 2, y], grid[x + 2, y + 2], grid[x, y + 2]]
            )
            dc = corners + corners
            if grid[x + 1, y + 1] == "A" and "MM" in dc and "SS" in dc:
                part2 += 1

    return Answer(part1, part2)
