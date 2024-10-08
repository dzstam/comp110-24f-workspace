"""EX02 - Chardle (A step towards Wordle)"""

__author__: str = "730461334"


def input_word() -> str:
    """checks word length"""
    word: str = input("Enter a 5-character word: ")
    word_length: int = len(word)
    if word_length != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        return word


def input_letter() -> str:
    """ "checks letter length"""
    letter: str = input("Enter a single character: ")
    letter_length: int = len(letter)
    if letter_length != 1:
        print("Error: Character must be a single character. ")
        exit()
    else:
        return letter


# this function needs to be separate from the others because the other two need to check whether the direction were followed
def contains_char(word: str, letter: str) -> None:
    """evaluates letter presence in word, and how many times"""
    print("Searching for " + letter + " in " + word)
    index: int = 0
    matching_characters: int = 0
    while index < len(word):  # make sure the index < len(word), not <=
        if word[index] == letter:
            print((letter) + " found at index " + str(index))
            matching_characters = matching_characters + 1
        index = index + 1
    if matching_characters == 0:  # this line must be separate from the while loop
        print("No instances of " + letter + " found in " + word)
    elif matching_characters == 1:
        print(str(matching_characters) + " instance of " + letter + " found in " + word)
    else:
        print(
            str(matching_characters) + " instances of " + letter + " found in " + word
        )


def main() -> None:  # need a main function to tie all functions together
    contains_char(word=input_word(), letter=input_letter())


# notice that word, though defined in input_word, must be reassigned an argument because it is not defined in this frame

if __name__ == "__main__":
    main()
