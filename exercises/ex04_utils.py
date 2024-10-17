"""List Unitlity Functions"""

__author__: str = "730461334"


def all(vals: list[int], integer: int) -> bool:
    """Determines if the list contains a specific integer"""
    if len(vals) == 0:
        return False
    for elem in vals:
        if elem != integer:
            return False
    return True  # don't use else, because it should return true if it does not return false, anyways


def max(vals: list[int]) -> int:
    """Identify the largest number in the list"""
    if len(vals) == 0:
        raise ValueError("max() arg is an empty List")
    largest: int = vals[
        0
    ]  # the largest must be the first number, because if the first element is negative, then 0 won't work
    for elem in vals:
        if elem > largest:
            largest = elem
            # can use elem to identify a number, since this is not a for ... range loop
    return largest


def is_equal(vals1: list[int], vals2: list[int]) -> bool:
    """Determines whether the lists are the same"""
    idx: int = 0
    # check lengths
    if len(vals1) != len(vals2):
        return False
    # if the a pair of numbers are different, return False
    while idx < len(vals1):
        if vals1[idx] != vals2[idx]:
            return False
        idx += 1
    # return True if the while loop does not uncover anything false
    return True


def extend(vals1: list[int], vals2: list[int]) -> None:
    for elem in vals2:
        vals1.append(elem)


# can't use a for loop without range because you need an index value
# must use for loop with range, and use the elem variable as an index, or use a while loop

my_list: list[int] = [1, 0, 1]
your_list: list[int] = [1, 0, 1]

# print(all(my_list, 4))
# print(is_equal(my_list, your_list))

# print(extend(my_list, your_list))
# print(my_list)
