"""Tea Party Exercise 01"""

__author__: str = "730461334"


def main_planner(guests: int) -> None:
    """Main planner to calculate cost based on numbers of tea bags and treats, which are based on the number of people attending"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# notice that you need to identify the parameters and argument each time you call a function!


def tea_bags(people: int) -> int:
    """defines tea bags according to the number of guests"""
    return int(people * 2)


def treats(people: int) -> int:
    """defines treats according to the number of guests"""
    return int(tea_bags(people=people) * 1.5)


# ^ this function call to tea_bags must use keyword argument, which specifies that people in this definition is the same as the people in the next definition
# the parameter of this definition is not tea bags (and if the functions were combined, then the code would be more difficult to update if the built-in numbers needed to be changed)


def cost(tea_count: int, treat_count: int) -> float:
    """defines the cost of tea bags and treats combined"""
    return float((0.5 * tea_count) + (0.75 * treat_count))


if __name__ == "main":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
