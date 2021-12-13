def get_binary_numbers():
    with open('input.txt') as f:
        numbers = [line.strip() for line in f.readlines()]
    return numbers


def get_oxygen_rating(numbers):
    idx = 0
    while len(numbers) != 1:
        ones = [num[idx] for num in numbers].count('1')
        dominant_num = '1' if ones >= (len(numbers) / 2) else '0'
        numbers = [num for num in numbers if num[idx] == dominant_num]
        idx += 1

    return numbers[0]


def get_co2_rating(numbers):
    idx = 0
    while len(numbers) != 1:
        zeros = [num[idx] for num in numbers].count('0')
        dominant_num = '0' if zeros <= (len(numbers) / 2) else '1'
        numbers = [num for num in numbers if num[idx] == dominant_num]
        idx += 1

    return numbers[0]


def main():
    numbers = get_binary_numbers()
    print(int(get_oxygen_rating(numbers), 2) * int(get_co2_rating(numbers), 2))


if __name__ == '__main__':
    main()
