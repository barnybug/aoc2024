from aoc2024 import day10

testdata = open("tests/input10.txt").read()


def test_01a():
    assert day10.solve("...0...\n...1...\n...2...\n6543456\n7.....7\n8.....8\n9.....9").part1 == 2


def test_01b():
    assert day10.solve(testdata).part1 == 36


def test_02():
    assert day10.solve(testdata).part2 == 81
