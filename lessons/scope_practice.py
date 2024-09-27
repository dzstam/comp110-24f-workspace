def remove_chars(msg: str, char: str) -> str:
    """Return a copy of a message with all instances of char removed"""
    copy: str = ""  # local variable
    index: int = 0  # local variable
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"  # this is a global variable
    print(remove_chars(word, "o"))
