__author__: str = "730461334"


def find_and_remove_max(vals: list[int]) -> int:
    if len(vals) == 0:
        return -1
    largest: int = vals[0]  # must be the first element
    for elem in vals:
        if elem > largest:
            largest = elem
            # can use elem to identify a number, since this is not a for ... range loop
    idx: int = 0
    while idx < len(vals):
        if vals[idx] == largest:
            vals.pop(idx)
            idx -= 1  # need to keep the index the same when an element is removed because otherwise, it moves on and skips the number that is in the removed element's place
        idx += 1
    return largest


my_list: list[int] = [10, 2, 3, 1, 10, 10]

print(find_and_remove_max(my_list))
print(my_list)
