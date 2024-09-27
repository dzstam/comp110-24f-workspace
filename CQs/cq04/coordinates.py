"""Coordinates"""

__author__: str = "730461334"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    index2: int = 0
    output: str = "("
    while index1 < len(xs):
        output = output + xs[index1] + ","
        while index2 < len(ys):
            output = output + ys[index2] + ")"
            index2 = index2 + 1
            print(output)
            output = "(" + xs[index1] + ","
        index1 = index1 + 1
        index2 = 0
        output = "("


# how get it to not return None


print(get_coords("hi", "bye"))
