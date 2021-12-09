# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def oc_add(memory: [int], index: int) -> int:
    memory[memory[index + 2]] = memory[memory[index]] + memory[memory[index + 1]]
    return index + 3


def oc_mul(memory: [int], index: int) -> int:
    memory[memory[index + 2]] = memory[memory[index]] * memory[memory[index + 1]]
    return index + 3


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
func_dict = {
    1: oc_add,
    2: oc_mul,
}


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def run_program(memory: [int]):
    ic = 0
    while ic < len(int_code_program):
        opcode = int_code_program[ic]
        if opcode == 99:
            break
        ic = func_dict[opcode](int_code_program, ic + 1)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
with open("day2_input.txt", "r") as file:
    int_code_program = [int(x) for x in file.read().split(',')]
# print(int_code_program)

code_backup = int_code_program.copy()

for noun in range(100):
    for verb in range(100):

        int_code_program[1] = noun
        int_code_program[2] = verb

        run_program(int_code_program)

        if int_code_program[0] == 19690720:
            print(100 * noun + verb)
            exit(0)

        int_code_program.clear()
        int_code_program.extend(code_backup)
