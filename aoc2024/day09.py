from dataclasses import dataclass

from .utils import Answer


def part1(input: str):
    it = map(int, input)
    blocks = []
    free = 0
    for n, i in enumerate(it):
        blocks.extend(n for _ in range(i))
        try:
            gap = next(it)
        except StopIteration:
            break
        free += gap
        blocks.extend(None for _ in range(gap))
    freemap = (i for i, b in enumerate(blocks) if b is None)

    for _ in range(free):
        block = blocks.pop()
        if block is None:
            continue
        gap = next(freemap)
        blocks[gap] = block

    return sum(a * b for a, b in enumerate(blocks) if b is not None)


@dataclass
class Node:
    """Linked list"""

    file_id: int | None
    size: int
    prev: "Node | None"
    next: "Node | None"


def display(node: Node):
    s = ""
    while node:
        for i in range(node.size):
            s += "." if node.file_id is None else str(node.file_id)
        node = node.next
    print(s)


def part2(input: str):
    it = map(int, input)
    first = None
    last = None
    file_ids = [(i // 2 if i % 2 == 0 else None, s) for i, s in enumerate(it)]

    for file_id, size in file_ids:
        node = Node(file_id, size, last, None)
        if last is None:
            first = node
        else:
            last.next = node
        last = node

    current = last
    while current != first:
        if current.file_id is None:
            current = current.prev
            continue

        # try to move current
        space = first
        prev = current.prev
        while space != current:
            if space.file_id is None and current.size <= space.size:
                # display(first)
                space.size -= current.size
                space.prev.next = current
                if current.next is None:  # end: just truncate
                    current.prev.next = None
                else:
                    if current.prev.file_id is None:  # increase previous space
                        current.prev.size += current.size
                        current.prev.next, current.next.prev = (
                            current.next,
                            current.prev,
                        )
                    elif current.next.file_id is None:  # increase following space
                        current.next.size += current.size
                        current.prev.next, current.next.prev = (
                            current.next,
                            current.prev,
                        )
                    else:  # create new space
                        new_space = Node(None, current.size, current.prev, current.next)
                        current.prev.next, current.next.prev = new_space, new_space
                current.prev = space.prev
                current.next = space
                space.prev = current
                # display(first)
                # print("----------------")
                break

            space = space.next

        current = prev

    n = first
    pos = 0
    total = 0
    while n:
        if n.file_id:
            total += sum(i * n.file_id for i in range(pos, pos + n.size))
        pos += n.size
        n = n.next

    return total


def solve(input: str):
    return Answer(part1(input), part2(input))
