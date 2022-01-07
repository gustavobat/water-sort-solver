from enum import Enum


# Rules:
# - Only the top fraction of each tube can be moved.
# - A fraction can be moved to the top of another fraction of the same color.
# - A fraction can be moved to an empty tube.

# Enum class that defines colors
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


# Create a list of colors out of integer values
def make_tube(color_values):
    assert all(1 <= el <= 18 for el in color_values), "Please enter color values from 1 to 18!"
    return list(map(Color, color_values))


# Create empty tube
def make_empty_tube():
    return list()


# Convert tube to string form
def tubes_to_string(tubes):
    s = ''
    for tube in tubes:
        for color in tube:
            s += str(color.value)
        s += ';'
    return s


# Check if all tubes are sorted
def is_sorted(tubes):
    for tube in tubes:
        # Check if tube has more than one color
        if len(set(tube)) > 1:
            return False
        # Check if tube is empty or full
        if len(tube) != 4 and len(tube) != 0:
            return False
    return True


# Check if the move from tubes[i] to tubes[j] is valid
def is_valid_move(tubes, i, j):

    # Can't move from and empty tube
    if len(tubes[i]) == 0:
        return False
    # Can't move to a full tube
    if len(tubes[j]) == 4:
        return False
    # If the source tube is solved, leave it alone
    if len(set(tubes[i])) == 1 and len(tubes[i]) == 4:
        return False
    # Don't move to empty tube if source tube is same colored
    if len(tubes[j]) == 0:
        if len(set(tubes[i])) <= 1:
            return False
        else:
            return True
    # Check color of top fractions
    return tubes[i][-1] == tubes[j][-1]


def main():
    tube1 = make_tube([1, 1, 2, 3])
    print(tube1)


if __name__ == "__main__":
    main()
