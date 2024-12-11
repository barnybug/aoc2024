from aoc2024 import day03

testdata = open("tests/input03.txt").read()
testdata2 = open("tests/input03b.txt").read()


def test_01():
    assert day03.solve(testdata).part1 == 161


def test_02():
    assert day03.solve(testdata2).part2 == 48
