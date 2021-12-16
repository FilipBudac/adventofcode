from dataclasses import dataclass
from typing import Union


def get_bits():
    with open('input.txt') as f:
        content = bytes.fromhex(f.read())
        bits = ''.join(map('{:08b}'.format, content))

    return bits


def sum_versions(packet):
    if packet.type_id == 4:
        return packet.version

    return packet.version + sum([sum_versions(other_packet) for other_packet in packet.content])


def check_first_bit(num):
    return num & 0b10000


@dataclass
class Packet:
    version: int
    type_id: int
    content: Union[int, list]


class PacketParser:
    def __init__(self, bits):
        self.bits = bits
        self.pos = 0

    def parse_num_of_packets(self, num):
        return [self.parse_packet() for _ in range(num)]

    def parse_length_of_packets(self, length):
        end = self.pos + length

        packets = []
        while self.pos < end:
            packets.append(self.parse_packet())

        return packets

    def parse_literal_content(self):
        group = 0b10000
        while check_first_bit(group):
            group = self.bits_2_dec(5)

        return None

    def parse_operator_content(self):
        len_type_id = self.bits_2_dec(1)
        if len_type_id == 1:
            packets_num = self.bits_2_dec(11)
            return self.parse_num_of_packets(packets_num)

        packets_len = self.bits_2_dec(15)
        return self.parse_length_of_packets(packets_len)

    def bits_2_dec(self, num):
        bits = self.bits[self.pos: self.pos + num]
        self.pos += num

        return int(bits, 2)

    def parse_packet_header(self):
        return self.bits_2_dec(3), self.bits_2_dec(3)

    def parse_packet_content(self, type_id):
        return self.parse_literal_content() if type_id == 4 else self.parse_operator_content()

    def parse_packet(self):
        version, type_id = self.parse_packet_header()
        content = self.parse_packet_content(type_id)

        return Packet(version, type_id, content)


def main():
    parser = PacketParser(get_bits())
    packet = parser.parse_packet()
    print(sum_versions(packet))


if __name__ == '__main__':
    main()
