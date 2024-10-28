"""Dictionary Utility Functions Exercise 06"""

__author__: str = "730461334"


def invert(input: dict[str, str]) -> dict[str, str]:
    """inverts keys and values. the keys of the input list becomes the values of the output list and vice versa"""
    # need a new dict because modifying the existing one during the for loop won't work
    inverted_dict: dict[str, str] = {}
    # check if there are duplicate vals
    # create an empty list that will be filled with seen values
    vals: list[str] = []
    for key in input:
        if input[key] in vals:
            raise KeyError("Duplicate keys are not possible!")
        vals.append(input[key])
    for key in input:
        inverted_dict[input[key]] = key
    return inverted_dict


"""testing invert"""
# my_dict: dict[str, str] = {"kris": "jordan", "michael": "jordan"}
# print(invert(my_dict))


def favorite_color(input: dict[str, str]) -> str:
    """returns the color that appears most frequently."""
    """if there is a tie, the color that appeared in the dict first is returned"""
    tally: dict[str, int] = {}
    most_favorite_color: str = ""
    biggest_number: int = 0
    for key in input:
        # adds a talley if the color is found
        if input[key] in tally:
            tally[input[key]] += 1
        if input[key] not in tally:
            tally[input[key]] = 1
    for key in tally:
        # find the color with the highest tally
        if tally[key] > biggest_number:
            most_favorite_color = key
            biggest_number = tally[key]
    print(tally)
    return most_favorite_color


"""testing favorite_color"""
# my_dict: dict[str, str] = {
#     "Marc": "yellow",
#     "Ezri": "blue",
#     "r": "blue",
#     "e": "green",
#     "w": "blue",
#     "v": "blue",
# }
# print(favorite_color(my_dict))
# i commented these all out using command + / (for furutre reference)


def count(input: list[str]) -> dict[str, int]:
    """each key is a unique value from the list"""
    """the value is the count of the times that value appeared"""
    tally: dict[str, int] = {}
    for elem in input:
        # adds a talley to existing elements in the dictionary
        if elem in tally:
            tally[elem] += 1
            # makes a new key
        if elem not in tally:
            tally[elem] = 1
    return tally


"""testing count"""
# my_list: list[str] = ["apple", "apple", "boy", "angry", "bad", "car"]
# print(count(my_list))


def alphabetizer(input_upper: list[str]) -> dict[str, list[str]]:
    """each key is a unique letter in the alphabet"""
    """each value is a list of words that begin with that letter"""
    input: list[str] = []
    for elem in input_upper:
        # makes a new input list with all lower case characters
        input.append(elem.lower())
    sorted_dict: dict[str, list[str]] = {}
    for elem in input:
        letter: str = elem[0]
        # sorted_dict[letter] = vals_list.append(elem)  # - can't assign because Argument of type "None" cannot be assigned to parameter "value" of type "list[str]" in function "__setitem__" ... "None" is not assignable to "list[str]"
        if letter not in sorted_dict:
            # adds a new key if letter is not present
            sorted_dict[letter] = [elem]
        if letter in sorted_dict:
            # appends the value if the key is present
            if elem not in sorted_dict[letter]:  # will not add repeats
                sorted_dict[letter].append(elem)
    return sorted_dict


"""testing alphabetizer"""
# my_list: list[str] = ["cherry", "cherry", "car"]
# print(alphabetizer(my_list))


def update_attendance(
    attendance_log: dict[str, list[str]], dow: str, name: str
) -> None:
    """Mutates attendance log to add a name to a specific day, if not already present."""
    if dow not in attendance_log:
        # new key with dow!
        # appends the name
        attendance_log[dow] = []
        attendance_log[dow].append(name)
    if (dow in attendance_log) and (name not in attendance_log[dow]):
        # existing key with dow!
        # appends the name if not already present
        attendance_log[dow].append(name)


"""testing update_attendance"""
# attendance_log: dict[str, list[str]] = {
#     "Monday": ["Vrinda", "Kaleb"],
#     "Tuesday": ["Alyssa"],
# }
# attendance_log: dict[str, list[str]] = {
#     "Monday": ["Anna"],
#     "Tuesday": ["Demetra"],
#     "Wednesday": ["Amena"],
#     "Thursday": ["Annabel"],
# }
# attendance_log: dict[str, list[str]] = {}
# update_attendance(attendance_log, "Tuesday", "Demetra")
# update_attendance(attendance_log, "Saturday", "Agatha")
# print(attendance_log)
