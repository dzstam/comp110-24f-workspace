"""File to define Fish class."""

__author__: str = "730461334"


class Fish:
    """Class for a single fish."""

    age: int

    def __init__(self) -> None:
        """Initializes the age of the fish."""
        self.age = 0
        return None

    def one_day(self) -> None:
        """Increases age by one day."""
        self.age += 1
        return None
