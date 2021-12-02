from dataclasses import dataclass

@dataclass
class StateMachine:
    memory = {"forward":0, "down":0}
    program: list[str]

    def run(self):
        """Run the program"""
        current_line = 0
        while current_line < len(self.program):
            instruction = self.program[current_line]

        
            if instruction.startswith("forward "):
                self.memory["forward"] = self.memory["forward"] + int(instruction[8])

            if instruction.startswith("down "):
                self.memory["down"] = self.memory["down"] + int(instruction[5])

            if instruction.startswith("up "):
                self.memory["down"] = self.memory["down"] - int(instruction[3])


            current_line += 1


@dataclass
class StateMachine2:
    memory = {"forward":0, "down":0, "aim":0, "depth":0}
    program: list[str]

    def run(self):
        """Run the program"""
        current_line = 0
        while current_line < len(self.program):
            instruction = self.program[current_line]

            
            if instruction.startswith("forward "):
                self.memory["forward"] = self.memory["forward"] + int(instruction[8])
                self.memory["depth"] += self.memory["aim"] * int(instruction[8])

            if instruction.startswith("down "):
                self.memory["aim"] = self.memory["aim"] + int(instruction[5])

            if instruction.startswith("up "):
                self.memory["aim"] = self.memory["aim"] - int(instruction[3])

    
            current_line += 1