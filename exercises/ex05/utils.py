"""List Unit Tests"""

__author__: str = "730461334"


def only_evens(vals: list[int]) -> list[int]:
    """takes a list and creates a new list of the even numbers only"""
    evens: list[int] = []
    # adds only even numbers to the new list
    for elem in vals:
        if elem % 2 == 0:
            evens.append(elem)
    return evens


def sub(vals: list[int], si: int, ei: int) -> list[int]:
    """make a new list of elements in the desired range"""
    sub: list[int] = []
    # changes the bounds to be within range, if necessary
    if si < 0:
        si = 0
    if ei > len(vals):
        ei = len(vals)
    # appends values in that range to a new list
    for idx in range(si, ei):
        sub.append(vals[idx])
    return sub


def add_at_index(vals: list[int], elem: int, idx: int) -> None:
    if idx < 0 or idx > len(vals):
        raise IndexError("Index is out of bounds for the input list")
    # adds a random value, which will be written over in the next step
    vals.append(0)
    # writes over the rightmost value with the value to the left, shifting the list over one index
    # goes from right to left
    for index in range(len(vals) - 1, idx, -1):
        # must start from the end of the list, to write over the indexes
        vals[index] = vals[index - 1]
    vals[idx] = elem


m: list[int] = [15, 17, 34, 46, 25]
a: list[int] = [1]
e: list[int] = []
# print(only_evens(my_list))
# print(sub(my_list, 1, 3))
add_at_index(m, 7, 1)
print(m)
