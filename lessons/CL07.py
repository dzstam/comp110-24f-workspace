def check_first_letter(word: str, letter: str) -> str:
    """Check if letter is the same as first character of word"""
    if word[0] == letter:
        return "match"
    else:
        return "no match"


print(check_first_letter(word="happy", letter="h"))
