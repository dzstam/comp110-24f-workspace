"""Challenge Question 3"""

__author__: str = "730461334"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # number of times there is a target character
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:  # evaluates the character at that position
            count = count + 1
        index = index + 1
    return count


print(num_instances)
