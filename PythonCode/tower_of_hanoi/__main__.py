"""My implementation of Tower of Hanoi in Python.

This algorithm is based on my own implementation of Stack (which in turn was
built on top of my implementation of singly linked list).

Rules (copied from: https://www.geeksforgeeks.org/):
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
The objective of the puzzle is to move the entire stack to rightmost rod,
obeying the following simple rules:
    1) Only one disk can be moved at a time.
    2) Each move consists of taking the upper disk from one of the stacks
    and placing it on top of another stack i.e. a disk can only be moved
    if it is the uppermost disk on a stack.
    3) No disk may be placed on top of a smaller disk.
"""

from tower_of_hanoi.text_gui import TextGUI


def main():
    gui = TextGUI()


if __name__ == "__main__":
    main()
