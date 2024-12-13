from aoc2024 import day07

testdata = open("tests/input07.txt").read()


def test_01():
    assert day07.solve(testdata).part1 == 3749


def test_02():
    assert day07.solve(testdata).part2 == 11387
