from aoc2024 import day01

testdata = open("tests/input01.txt").read()


def test_01():
    assert day01.solve(testdata).part1 == 11


def test_02():
    assert day01.solve(testdata).part2 == 31
