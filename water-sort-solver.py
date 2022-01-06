from enum import Enum


# Rules:
# - Only the top ball of each stack can be moved.
# - A ball can be moved to the top of another ball of the same colour
# - A ball can be moved to an empty stack.


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    WHITE = 5
    GREY = 6
    PINK = 7
    DARK_RED = 8
    DARK_GREEN = 9
    DARK_BLUE = 10
    DARK_YELLOW = 11
    LIGHT_RED = 12
    LIGHT_GREEN = 13
    LIGHT_BLUE = 14
    LIGHT_YELLOW = 15


def make_tube(color_values):
    return list(map(Color, color_values))


def main():
    tube1 = make_tube([1, 1, 2, 3])
    print(tube1)


if __name__ == "__main__":
    main()
