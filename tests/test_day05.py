from aoc2024 import day05

testdata = open("tests/input05.txt").read()


def test_01():
    assert day05.solve(testdata).part1 == 143


def test_02():
    assert day05.solve(testdata).part2 == 123
