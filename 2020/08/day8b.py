from copy import deepcopy


def loop(instructions):
    c = acc = 0
    seen = set()
    while c < len(instructions) and c not in seen:
        ins, val = instructions[c]
        seen.add(c)
        if ins == 'acc':
            acc += int(val)
        if ins == 'jmp':
            c += int(val) - 1
        c += 1
    return acc, c


def find_bad_instruction(ins_pair, instructions):
    ins, idx = ins_pair
    if ins == 'jmp':
        instructions[idx][0] = 'nop'
    if ins == 'nop':
        instructions[idx][0] = 'jmp'
    return loop(instructions)


with open('input.txt') as file:
    instructions = [line.strip().split(' ') for line in file]

switchable_ins = [(ins, idx) for idx, (ins, _) in enumerate(instructions) if ins in ['jmp', 'nop']]
for ins_pair in switchable_ins:
    acc, c = find_bad_instruction(ins_pair, deepcopy(instructions))
    if c == len(instructions):
        print(acc)
        break
