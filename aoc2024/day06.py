from .utils import Answer, Point

dirs = [Point.U, Point.R, Point.D, Point.L]


def traverse(blocks, start, d, width, height, extra=None, path=None):
    pos = start
    visited = {(pos, d)}
    while True:
        npos = pos + dirs[d]
        if npos.x < 0 or npos.x >= width or npos.y < 0 or npos.y >= height:
            break
        if npos in blocks or npos == extra:
            d = (d + 1) % 4
        else:
            pos = npos
            key = (pos, d)
            if path is not None:
                path.append(key)
            if key in visited:
                return True  # looped
            visited.add(key)

    return False


def solve(input: str):
    grid = input.splitlines()
    y = next(i for i, line in enumerate(grid) if "^" in line)
    x = grid[y].index("^")
    start = Point(x, y)
    blocks = {(x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == "#"}
    width, height = len(grid[0]), len(grid)
    path = []
    traverse(blocks, start, 0, width, height, path=path)
    part1 = len({pos for pos, _ in path})
    part2 = 0
    for start, d in path:
        extra = start + dirs[d]
        if extra in blocks:
            continue
        if traverse(blocks, start, d, width, height, extra):
            part2 += 1

    return Answer(part1, part2)
