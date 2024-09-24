"""Guessing Game CQ02"""

__author__: str = "730461334"


def guess_a_number() -> None:
    secret: int = (
        7  # make sure you define as an integer, because you will be evaluating this
    )
    x: int = int(
        input("Guess a number:")
    )  # make sure you define this as an integer in this way -- define the integer twice!!
    print("Your guess was " + str(x))
    if x == secret:
        print("You got it!")
    elif x <= secret:
        print("Your guess was too low! The secret number is " + str(secret))
    # elif x >= secret:
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
