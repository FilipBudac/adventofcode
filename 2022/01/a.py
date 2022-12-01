with open('input.txt') as file:
    elfs = (map(int, batch.rstrip().split('\n')) for batch in file.read().split("\n\n"))

print(max(sum(elf) for elf in elfs))
