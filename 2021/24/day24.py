MAX_NUM = 9


def get_instruction_chunks():
    with open("input.txt") as f:
        instruction_chunks = f.read().split("inp w\n")
    return instruction_chunks


def monad(instruction_chunks):
    z = []
    model_num = len(instruction_chunks) * [0]
    for i, instruction_chunk in enumerate(instruction_chunks[1:]):
        instructions = [instructions.split(' ') for instructions in instruction_chunk.split('\n')]

        y_add = int(instructions[14][-1])
        if int(instructions[3][-1]) != 26:  # or == 1
            z.append((i, y_add))
        # apply mysterious restriction
        else:
            j, y_add = z.pop()
            x_add = int(instructions[4][-1])

            diff = x_add + y_add
            if diff < 0:
                model_num[i] = MAX_NUM + diff
                model_num[j] = MAX_NUM
            elif diff > 0:
                model_num[i] = MAX_NUM
                model_num[j] = MAX_NUM - diff
            else:
                model_num[i] = model_num[j] = MAX_NUM

    return model_num


def main():
    print(''.join(map(str, monad(get_instruction_chunks()))))


if __name__ == '__main__':
    main()
