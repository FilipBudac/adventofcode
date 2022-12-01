import heapq

with open('input.txt') as file:
    elfs = (map(int, batch.rstrip().split('\n')) for batch in file.read().split("\n\n"))

print(sum(heapq.nlargest(3, (sum(elf) for elf in elfs))))
