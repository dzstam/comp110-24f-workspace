def get_first(vals: list[str]) -> str:
    """return first element of a list"""
    if len(vals) == 0:
        return ""
    return vals[0]


def remove_first(vals: list[str]) -> None:
    """remove the first element of a list"""
    vals.pop(0)


def get_and_remove_first(vals: list[str]) -> str:
    """return the first element and remove the first element"""
    first_element: str = vals[0]  # save the value to return later
    vals.pop(0)
    return first_element


# can't be the other way around, because return must be the last thing


my_list: list[str] = ["comp", "110", "class"]

print(get_first(my_list))
print(remove_first(my_list))
print(get_and_remove_first(my_list))

# test in repl
# from lessons.unit_tests.list_fns import get_and_remove_first
