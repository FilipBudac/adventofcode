def get_signal_patterns():
    with open('input.txt') as f:
        patterns = [line.split(' | ') for line in f.readlines()]
        patterns = [[inputs.split(' '), outputs.split(' ')] for inputs, outputs in patterns]

    return patterns


def b():
    c = 0
    for digits, outputs in get_signal_patterns():
        digits_table = {}
        for digit in digits:
            digit = set(digit)
            if len(digit) == 2:
                digits_table[1] = digit
            if len(digit) == 3:
                digits_table[7] = digit
            if len(digit) == 4:
                digits_table[4] = digit
            if len(digit) == 7:
                digits_table[8] = digit

        for digit in digits:
            digit = set(digit)
            if digit in digits_table.values():
                continue
            if len(digit) == 5 and len(digit.intersection(digits_table[7])) == 3:
                digits_table[3] = digit
            if len(digit) == 6 and len(digit.intersection(digits_table[4])) == 4:
                digits_table[9] = digit
            if len(digit) == 6 and len(digit.intersection(digits_table[7])) == 2:
                digits_table[6] = digit

        for digit in digits:
            digit = set(digit)
            if digit in digits_table.values():
                continue
            if len(digit) == 5 and len(digit.intersection(digits_table[4])) == 3 and len(digit.intersection(digits_table[3])) != 5:
                digits_table[5] = digit

        for digit in digits:
            digit = set(digit)
            if digit in digits_table.values():
                continue
            if len(digit) == 6 and digit not in digits_table.values():
                digits_table[0] = digit
            if len(digit) == 5 and digit not in digits_table.values():
                digits_table[2] = digit

        res = ''
        for output in outputs:
            output = set(output.strip())
            for k, d in digits_table.items():
                if output == d:
                    res += str(k)
        c += int(res)
    print(c)


def main():
    b()


if __name__ == '__main__':
    main()
