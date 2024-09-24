"""EX02 - Chardle (A step towards Wordle)"""

__author__: str = "730461334"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    word_length: int = len(word)
    if (
        word_length != 5
    ):  # the boolean operator 1= could be switched to = if the if and else statements were switched
        print("Error: Word must contain 5 charcters.")
        exit()
    else:
        return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    letter_length: int = len(letter)
    if letter_length != 1:
        print("Error: Character must be a single character. ")
        exit()
    else:
        return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    index: int = 0
    matching_characters: int = 0
    while index < len(word):
        if word[index] == letter:
            print(str(letter) + " found at index " + str(index))
            matching_characters = matching_characters + 1
        index = index + 1
    if matching_characters != 0:
        print(
            str(matching_characters)
            + " instances of "
            + str(letter)
            + " found in "
            + (word)
        )
    else:
        print("No instances of " + str(letter) + " found in " + str(word))


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
