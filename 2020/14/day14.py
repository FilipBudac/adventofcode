import re
import collections


def dec_2_bin(dec_num):
    return list(format(dec_num, 'b').zfill(36))


def bin_2_dec(bin_num):
    return int(''.join(bin_num), 2)


def add_val_to_mask(mask, bin_num):
    return [m if m != 'X' else b for m, b in zip(mask, bin_num)]


def write_2_mem(mem, bin):
    mem[addr] = bin_2_dec(bin)


mem = collections.defaultdict(int)
with open('input.txt') as file:
    for line in file:
        if re.match(r'mask = (0|1|X)+', line):
            mask = list(line[7:].rstrip())
            continue
        addr, val = map(int, re.findall(r'\d+', line))
        res = add_val_to_mask(mask, dec_2_bin(addr))

        write_2_mem(mem, res)

print(sum(mem.values()))
