import pathlib
import sys
import numpy as np


def parse(puzzle_input):
    """Parse input"""
    s = puzzle_input.split()
    numbers = list(s[0].split(","))
    numbers = list(map(int, numbers))
    boards = [s[1:][i : i + 5] for i in range(0, len(s[1:]), 5)]
    boards = [boards[i : i + 5] for i in range(0, len(boards), 5)]
    boards = np.array(boards).astype("int64")
    return numbers, boards


def part1(data):
    """Solve part 1"""
    numbers, boards = data
    mask = np.full(boards.shape, False, dtype="bool")
    for number in numbers:
        for i in range(len(boards)):
            mask[i] = (boards[i] == number) + mask[i]
            if np.any(np.sum(mask[i], axis=0) == 5) or np.any(
                np.sum(mask[i], axis=1) == 5
            ):
                return np.sum(boards[i][~mask[i]]) * number


def part2(data):
    """Solve part 2"""
    # find last board to win
    numbers, boards = data
    mask = np.full(boards.shape, False, dtype="bool")
    for number in numbers:
        for i in range(len(boards)):
            mask[i] = (boards[i] == number) + mask[i]
            if np.any(np.sum(mask[i], axis=0) == 5) or np.any(
                np.sum(mask[i], axis=1) == 5
            ):
                return np.sum(boards[i][~mask[i]]) * number


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        # print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
