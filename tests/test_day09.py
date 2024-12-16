from aoc2024 import day09

testdata = open("tests/input09.txt").read()


def test_01():
    assert day09.solve(testdata).part1 == 1928


def test_02():
    assert day09.solve(testdata).part2 == 2858
