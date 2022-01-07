from enum import Enum


# Rules:
# - Only the top fraction of each tube can be moved.
# - A fraction can be moved to the top of another fraction of the same color.
# - A fraction can be moved to an empty tube.


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    WHITE = 5
    GREY = 6
    ORANGE = 7
    PINK = 8
    PURPLE = 9
    BROWN = 10
    DARK_RED = 11
    DARK_GREEN = 12
    DARK_BLUE = 13
    DARK_YELLOW = 14
    LIGHT_RED = 15
    LIGHT_GREEN = 16
    LIGHT_BLUE = 17
    LIGHT_YELLOW = 18


def make_tube(color_values):
    return list(map(Color, color_values))


def make_empty_tube():
    return list()


def tubes_to_string(tubes):
    s = ''
    for tube in tubes:
        for color in tube:
            s += str(color.value)
        s += ';'
    return s


def is_sorted(tubes):
    for tube in tubes:
        # Check if tube has more than one color
        if len(set(tube)) > 1:
            return False
        # Check if tube is empty or full
        if len(tube) != 4 or len(tube) != 0:
            return False
    return True


def main():
    tube1 = make_tube([1, 1, 2, 3])
    print(tube1)


if __name__ == "__main__":
    main()
