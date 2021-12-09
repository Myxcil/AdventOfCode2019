# -------------------------------------------------------------------------------------------------------------------------------------------------------------
class CPU:
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    class Instruction:
        def __init__(self, function, param_count: int, dst_count: int):
            self.function = function
            self.param_count = param_count
            self.dst_count = dst_count

    def __init__(self, memory: [int]):
        self.ic = 0
        self.memory = memory
        self.stack = []
        self.current_input = 1
        self.debug_print = False

        self.func_map: dict[int, CPU.Instruction] = {
            1: CPU.Instruction(self.add, 2, 1),
            2: CPU.Instruction(self.mul, 2, 1),
            3: CPU.Instruction(self.inp, 0, 1),
            4: CPU.Instruction(self.out, 0, 1),
            5: CPU.Instruction(self.jit, 2, 0),
            6: CPU.Instruction(self.jif, 2, 0),
            7: CPU.Instruction(self.lss, 2, 1),
            8: CPU.Instruction(self.equ, 2, 1),
        }

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def run(self):
        self.ic = 0
        param_mode = [0, 0, 0]
        while self.ic < len(self.memory):
            old_ic = self.ic
            opcode = self.memory[self.ic]
            self.ic += 1
            if opcode == 99:
                break

            modes = 0
            if opcode > 99:
                modes = opcode / 100
                opcode %= 100
            for i in range(3):
                param_mode[i] = int(modes % 10)
                modes /= 10

            cmd: CPU.Instruction = self.func_map[opcode]

            for i in range(cmd.param_count):
                param_value = self.memory[self.ic]
                if param_mode[i] == 0:
                    param_value = self.memory[param_value]
                self.stack.append(param_value)
                self.ic += 1

            for i in range(cmd.dst_count):
                self.stack.append(self.memory[self.ic])
                self.ic += 1

            if self.debug_print:
                print(f'ic={old_ic} op={cmd.function} pm={param_mode} st={self.stack}')

            cmd.function()
            assert len(self.stack) == 0

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def add(self):
        lhs = self.stack.pop(0)
        rhs = self.stack.pop(0)
        dst = self.stack.pop(0)
        self.memory[dst] = lhs + rhs

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def mul(self):
        lhs = self.stack.pop(0)
        rhs = self.stack.pop(0)
        dst = self.stack.pop(0)
        self.memory[dst] = lhs * rhs

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def inp(self):
        dst = self.stack.pop(0)
        self.memory[dst] = self.current_input

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def out(self):
        dst = self.stack.pop(0)
        print(self.memory[dst])

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def jit(self):
        lhs = self.stack.pop(0)
        rhs = self.stack.pop(0)
        if lhs != 0:
            self.ic = rhs

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def jif(self):
        lhs = self.stack.pop(0)
        rhs = self.stack.pop(0)
        if lhs == 0:
            self.ic = rhs

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def lss(self):
        lhs = self.stack.pop(0)
        rhs = self.stack.pop(0)
        dst = self.stack.pop(0)
        if lhs < rhs:
            self.memory[dst] = 1
        else:
            self.memory[dst] = 0

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def equ(self):
        lhs = self.stack.pop(0)
        rhs = self.stack.pop(0)
        dst = self.stack.pop(0)
        if lhs == rhs:
            self.memory[dst] = 1
        else:
            self.memory[dst] = 0


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
with open("day5_input.txt", "r") as file:
    int_code_program = [int(x) for x in file.read().split(',')]
backup_code = int_code_program.copy()

print("Part One")
cpu = CPU(int_code_program)
cpu.current_input = 1
cpu.run()

print("Part Two")
int_code_program = backup_code.copy()
cpu = CPU(int_code_program)
cpu.current_input = 5
cpu.run()