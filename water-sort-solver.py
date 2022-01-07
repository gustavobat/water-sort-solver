from enum import Enum
import copy


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


# Solve puzzle
def solve(tubes, visited, answer):
    tube_to_string = tubes_to_string(tubes)
    visited.add(tube_to_string)
    n_tubes = len(tubes)
    for i in range(n_tubes):
        for j in range(n_tubes):
            if i == j:
                continue
            if is_valid_move(tubes, i, j):
                # Create new tube configuration
                new_tubes = copy.deepcopy(tubes)
                new_tubes[j].append(new_tubes[i].pop())
                if is_sorted(new_tubes):
                    # Update answer
                    answer.append([i, j, 1])
                    return True
                if tubes_to_string(new_tubes) not in visited:
                    solve_for_rest = solve(new_tubes, visited, answer)
                    if solve_for_rest:
                        answer.append([i, j, 1])
                        return True
    return False


def interpret_answer(answer):
    simplified_answer = [answer[0]]
    for move in answer[1:]:
        if move[0] == simplified_answer[-1][0] and move[1] == simplified_answer[-1][1]:
            simplified_answer[-1][2] += 1
        else:
            simplified_answer.append(move.copy())

    for move in reversed(simplified_answer):
        text = "Move tube " + str(move[0] + 1) + " to " + str(move[1] + 1) + " "
        text += str(move[2]) + " time(s)."
        print(text)


def main():
    tube1 = make_tube([2, 3, 3, 3])
    tube2 = make_tube([4, 3, 1, 4])
    tube3 = make_tube([4, 2, 2, 4])
    tube4 = make_tube([1, 1, 1, 2])
    tube5 = make_empty_tube()
    tube6 = make_empty_tube()

    tubes = [tube1, tube2, tube3, tube4, tube5, tube6]
    answer = list()
    visited = set()

    solve(tubes, visited, answer)
    interpret_answer(answer)


if __name__ == "__main__":
    main()
