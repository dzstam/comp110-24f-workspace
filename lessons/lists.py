"""Basic syntax of lists"""

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

my_numbers.append(1.5)  # add item to list

game_points: list[int] = [102, 86, 94]  # create an already populated list

game_points[1] = 72

print(my_numbers)
print(game_points)

# subscription notation / indexing
print(game_points[1])
# or
last_game: int = game_points[2]
print(last_game)


# getting the length of the list
print(len(game_points))

# remove items from a list
# game_points.pop(2)
# print(game_points)

# DIRECTIONS
# write a function called display
# input: list(int)
# return none
# loop over the input and print every value
# use game_points

print("while loop below:")


def display(input: list[int]) -> None:
    # see how the parameter changes because the argument is a list
    index: int = 0
    while index < len(input):
        print(input[index])
        index = index + 1


print(display(input=game_points))
