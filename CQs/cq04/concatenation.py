"""Concatenation"""

__author__: str = "730461334"


def concat(word1: str, word2: str) -> str:
    # input1: str = input("")
    # input2: str = input()
    combined: str = ""
    combined = word1 + word2
    return combined


word1: str = "happy"
word2: str = "tuesday"

if (
    __name__ == "__main__"
):  # adding this prevents the call from being run when this file is imported
    print(concat(word1, word2))
