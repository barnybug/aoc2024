from aoc2024 import day08

testdata = open("tests/input08.txt").read()


def test_01():
    assert day08.solve(testdata).part1 == 14


def test_02():
    assert day08.solve(testdata).part2 == 34
