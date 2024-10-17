"""Summing the elements of a list using different loops"""

__author__: str = "730461334"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return float(sum)


# print(w_sum(my_list))


def f_sum(vals: list[float]) -> float:
    sum: float = 0
    for elem in vals:
        sum += elem
    return sum


# print(f_sum(my_list))


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0
    for elem in range(0, len(vals)):
        sum += vals[
            elem
        ]  # you can't just add up elem, because it will add 0+1+2. You have to use elem to specify the number in the list
    return sum


my_list: list[float] = [1.1, 0.9, 1.0]
empty_list: list[float] = []
print(f_range_sum(my_list))
# prints as an int, not a float
