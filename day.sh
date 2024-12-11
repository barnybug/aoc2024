#!/usr/bin/env bash

today=$(date +%02d)
stoday=$(date +%1d)
day="${1:-$today}"
sday="${1:-$stoday}"
testinput="tests/input$day.txt"
input="aoc2024/inputs/input$day.txt"
daycode="aoc2024/day$day.py"
testcode="tests/test_day$day.py"

touch $testinput $input
if [ ! -f "$testcode" ]; then
    cat <<EOF > $testcode
from aoc2024 import day$day

testdata = open("tests/input$day.txt").read()


def test_01():
    assert day$day.solve(testdata).part1 == None


def test_02():
    assert day$day.solve(testdata).part2 == None
EOF
fi
if [ ! -f "$daycode" ]; then
    cat <<EOF > $daycode
from .utils import Answer

def solve(input: str):
    return Answer(0, 0)
EOF
fi

zeditor $input $testinput $testcode $daycode
xdg-open https://adventofcode.com/2024/day/$sday >/dev/null
echo
echo "go!"
