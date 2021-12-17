import re
from dataclasses import dataclass


def get_trench_area():
    with open('input.txt') as f:
        point_x, point_y = [list(map(int, group)) for group in re.findall(r'(\d+|-\d+)..(\d+|-\d+)', f.read())]
    return point_x, point_y


@dataclass
class Probe:
    x: int
    y: int
    vel_x: int
    vel_y: int

    def can_hit_target(self, max_x, min_y):
        return self.x <= max_x and self.y >= min_y

    def is_target_hit(self, min_x, max_x, min_y, max_y):
        return max_x >= self.x >= min_x and max_y >= self.y >= min_y

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        if self.vel_x > 0:
            self.vel_x -= 1
        self.vel_y -= 1


def main():
    point_x, point_y = get_trench_area()
    min_x, max_x = point_x
    min_y, max_y = point_y

    hits = 0
    for vel_y in range(min_y, -(min_y - 1)):
        for vel_x in range(0, max_x + 1):
            probe = Probe(0, 0, vel_x, vel_y)
            while probe.can_hit_target(max_x, min_y):
                probe.move()
                if probe.is_target_hit(min_x, max_x, min_y, max_y):
                    hits += 1
                    break
    print(hits)


if __name__ == '__main__':
    main()
