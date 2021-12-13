def get_numbers():
    with open('input.txt') as f:
        numbers = [int(num) for num in f.readlines()]
    return numbers


def main():
    numbers = get_numbers()
    shifted_numbers = numbers[3:]
    print(sum(1 if other > num else 0 for num, other in zip(numbers, shifted_numbers)))


if __name__ == '__main__':
    main()
