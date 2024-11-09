"""File to define Bear class."""

__author__: str = "730461334"


class Bear:
    """class defining an individual Bear."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initializes Bear with age and hunger score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Increases age by one day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increases hunger score based on the number of fish eaten."""
        self.hunger_score += num_fish  # will draw from Fish in the River
        return None
