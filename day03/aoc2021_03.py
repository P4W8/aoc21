import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1"""
    most_common = [0] * len(data[0])
    for line in data:
        for i, char in enumerate(line):
            if char == "1":
                most_common[i] += 1
            else:
                most_common[i] -= 1
    gamma = int("".join(["1" if x > 0 else "0" for x in most_common]), 2)
    epsillon = gamma ^ int("1" * len(data[0]), 2)
    return gamma * epsillon


def part2(data):
    """Solve part 2"""
    oxygen_data = data.copy()
    oxy_count = 0
    most_common = [0] * len(oxygen_data[0])
    while len(oxygen_data) > 1:
        for line in oxygen_data:
            for i, char in enumerate(line):
                if char == "1":
                    most_common[i] += 1
                else:
                    most_common[i] -= 1
        most_common = ["1" if x >= 0 else "0" for x in most_common]
        oxygen_data = list(
            filter(lambda x: x[oxy_count] == most_common[oxy_count], oxygen_data)
        )
        oxy_count += 1
        most_common = [0] * len(oxygen_data[0])
    co2_data = data.copy()
    co2_count = 0
    most_common = [0] * len(co2_data[0])
    while len(co2_data) > 1:
        for line in co2_data:
            for i, char in enumerate(line):
                if char == "1":
                    most_common[i] += 1
                else:
                    most_common[i] -= 1
        most_common = ["0" if x >= 0 else "1" for x in most_common]
        co2_data = list(
            filter(lambda x: x[co2_count] == most_common[co2_count], co2_data)
        )
        co2_count += 1
        most_common = [0] * len(co2_data[0])
    return int(oxygen_data[0], 2) * int(co2_data[0], 2)


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
