from dataclasses import dataclass
from typing import Union


def get_snails():
    with open('input.txt') as f:
        snails = [eval(line) for line in f.readlines()]
    return snails


def magnitude(snail):
    if snail.left is None and snail.right is None:
        return snail.val

    return 3 * magnitude(snail.left) + 2 * magnitude(snail.right)


@dataclass
class Node:
    val: int = 0
    parent: 'Node' = None
    left: Union['Node', None] = None
    right: Union['Node', None] = None

    @classmethod
    def from_snail(cls, item, parent=None):
        if isinstance(item, int):
            return Node(parent=parent, val=item)

        left, right = item
        node = Node(parent=parent)
        node.left = Node.from_snail(left, parent=node)
        node.right = Node.from_snail(right, parent=node)

        return node

    def explode(self, depth=0):
        if self.left is None and self.right is None:
            return

        if depth > 3:
            return self.apply_explosion()

        self.left.explode(depth + 1)
        self.right.explode(depth + 1)

    def split(self):
        if self.val > 9:
            return self.apply_split()

        if self.left is not None:
            if self.left.split():
                return True

        if self.right is not None:
            if self.right.split():
                return True

        return False

    def apply_split(self):
        left = self.val // 2
        right = self.val - left
        self.left = Node(parent=self, val=left)
        self.right = Node(parent=self, val=right)
        self.val = 0

        return True

    def apply_explosion(self):
        self.parent.add_2_left_number(self.left.val, self, True)
        self.parent.add_2_right_number(self.right.val, self, True)

        self.val = 0
        self.left = None
        self.right = None

    def add_2_right_number(self, val, child, right):
        if right:
            if self.right is None or self.right is child:
                if self.parent is not None:
                    self.parent.add_2_right_number(val, self, True)
                return

            self.right.add_2_right_number(val, self, False)
            return

        if self.left is None:
            self.val += val
            return

        self.left.add_2_right_number(val, self, False)

    def add_2_left_number(self, val, child, left):
        if left:
            if self.left is None or self.left is child:
                if self.parent is not None:
                    self.parent.add_2_left_number(val, self, True)
                return
            self.left.add_2_left_number(val, self, False)
            return

        if self.right is None:
            self.val += val
            return

        self.right.add_2_left_number(val, self, False)


def main():
    snails = get_snails()

    max_magnitude = 0
    for snail in snails:
        for other_snail in snails:
            new_snail = Node(left=Node.from_snail(snail), right=Node.from_snail(other_snail))
            new_snail.left.parent = new_snail
            new_snail.right.parent = new_snail

            new_snail.explode()
            while new_snail.split():
                new_snail.explode()

            max_magnitude = max(max_magnitude, magnitude(new_snail))

    print(max_magnitude)


if __name__ == '__main__':
    main()
