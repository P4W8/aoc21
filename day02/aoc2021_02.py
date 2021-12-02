import pathlib
import sys
from submarine import SubmarinePart1, SubmarinePart2


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1"""
    m = SubmarinePart1(data)
    m.run()
    return m.memory["forward"] * m.memory["down"]


def part2(data):
    """Solve part 2"""
    m = SubmarinePart2(data)
    m.run()
    return m.memory["forward"] * m.memory["depth"]


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
