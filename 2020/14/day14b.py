import collections
import itertools
import re


def dec_2_bin(dec_num):
    return list(format(dec_num, 'b').zfill(36))


def bin_2_dec(bin_num):
    return int(''.join(bin_num), 2)


def add_val_to_mask(mask, bin_num):
    return [m if m != '0' else b for m, b in zip(mask, bin_num)]


def write_2_mem(mem, bin):
    mem_writes = itertools.product('01', repeat=bin.count('X'))
    for write in map(iter, mem_writes):
        res = [next(write) if char == 'X' else char for char in bin]
        mem[bin_2_dec(res)] = val


mem = collections.defaultdict(int)
with open('input.txt') as file:
    for line in file:
        if re.match(r'mask = (0|1|X)+', line):
            mask = list(line[7:].rstrip())
            continue
        addr, val = map(int, re.findall(r'\d+', line))
        bin = add_val_to_mask(mask, dec_2_bin(addr))

        write_2_mem(mem, bin)

print(sum(mem.values()))
