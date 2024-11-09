"""River Simulation."""

__author__: str = "730461334"

from exercises.ex07.river import River

my_river: River = River(10, 2)
# my_river.view_river()
# my_river.one_river_week()
# print(my_river.check_ages())
# ^ probably shouldn't be printing that

# print(len(my_river.fish))
# my_river.remove_fish(3)
# print(len(my_river.fish))

print(my_river.bears_eating())
print(len(my_river.fish))
