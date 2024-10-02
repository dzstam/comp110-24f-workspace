"""Wordle"""

__author__: str = "730461334"


def input_guess(secret_word_len: int) -> str:
    """prompts the user to enter a guess until it is the correct length"""
    # secret_word_len: int = len(secret)
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} characters! Try again: ")
    return guess  # returns guess now so that we can assign this function to guess later


def contains_char(secret_word: str, char_guess: str) -> bool:
    """tests each index to see if one matches the secret word"""
    assert len(char_guess) == 1  # error will be raised if this is not true
    index1: int = 0
    matching_characters: int = 0
    while index1 < len(secret_word):
        if (
            secret_word[index1] == char_guess
        ):  # if a letter in the word = the intended character
            matching_characters = matching_characters + 1
        index1 = index1 + 1
    if matching_characters != 0:
        return True
    else:
        return False


# print(input_guess(secret_word_len=6))
# print(contains_char(secret_word="abc", char_guess="a"))

# type this into the REPL to use the function there
# from exercises.ex03_wordle import contains_char


def emojified(guess: str, secret_word: str) -> str:
    """compare two strings and return a string of emojis"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_line: str = ""
    index2: int = 0
    while index2 < len(guess):
        if guess[index2] == secret_word[index2]:
            emoji_line = emoji_line + GREEN_BOX
        elif contains_char(
            secret_word, guess[index2]
        ):  # if the word contains this letter, guess[index2]
            emoji_line = emoji_line + YELLOW_BOX
        else:  # the letter is not contained in the word
            emoji_line = emoji_line + WHITE_BOX
        index2 = index2 + 1
    return emoji_line  # return, don't print since you are printing later


# print(emojified(guess="dream", secret_word="crara"))
# emojified(guess="hello", secret_word="world")


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    index3: int = 0
    win: bool = False
    while index3 < 6 and not win:
        print(f"=== Turn {index3 + 1}/6 ===")
        guess = input_guess(
            len(secret)
        )  # don't just run input_guess, but redefine guess using this function. This is why guess was returned earlier.
        print(emojified(guess, secret))
        index3 += 1
        if guess == secret:
            win = True
            print(f"You won in {index3}/6 turns!")

    if not win:
        print("X/6 - Sorry, try again tomorrow!")


# (main(secret="codes"))
# this ^ is something you can just paste into the REPL (without the print)

if __name__ == "__main__":
    main(secret="codes")
