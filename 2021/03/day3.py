def get_binary_numbers():
    with open('input.txt') as f:
        numbers = [line.strip() for line in f.readlines()]
    return numbers


def main():
    numbers = get_binary_numbers()
    transposed_numbers = map(list, zip(*numbers))

    gama_rate = epsilon_rate = ''
    for number in transposed_numbers:
        ones = number.count('1')
        gama_rate += '1' if ones > (len(numbers) / 2) else '0'
        epsilon_rate += '0' if ones > (len(numbers) / 2) else '1'

    print(int(gama_rate, 2) * int(epsilon_rate, 2))


if __name__ == '__main__':
    main()
