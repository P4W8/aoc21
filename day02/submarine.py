from dataclasses import dataclass


@dataclass
class Submarine:
    memory: dict[str, int]
    program: list[str]

    def run(self):
        """Run the program"""
        current_line = 0
        while current_line < len(self.program):
            instruction = self.program[current_line]

            if instruction.startswith("forward "):
                self.memory["forward"] += int(instruction[8])
                self.memory["depth"] += self.memory["aim"] * int(instruction[8])

            if instruction.startswith("down "):
                self.memory["aim"] += int(instruction[5])
                self.memory["down"] += int(instruction[5])

            if instruction.startswith("up "):
                self.memory["aim"] -= int(instruction[3])
                self.memory["down"] -= int(instruction[3])

            current_line += 1
