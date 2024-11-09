"""File to define River class."""

__author__: str = "730461334"


from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Class to describe the river and how the population of fish and bears change."""

    day: int  # day of river's lifecycle
    bears: list[Bear]  # population of bears
    fish: list[Fish]  # population of fish

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(
                Fish()
            )  # adds age of fish into the list of fish, stopping at the number of fish avail
        for _ in range(0, num_bears):
            self.bears.append(Bear())  # adds age of bears into the list of bears

    def check_ages(self) -> None:
        """Eliminates fish over 3 and bears over 5."""
        correct_ages: list[Fish] = []
        for fish in self.fish:  # for each fish (Fish()) in the list
            if fish.age <= 3:
                # if Fish.age is less than 3 - need to use fish.age to use the age int value for this if statement
                correct_ages.append(fish)
                # add this element to the new list - use object type here
        self.fish = correct_ages
        correct_ages2: list[Bear] = []
        for bears in self.bears:  # for each fish (Fish()) in the list
            if bears.age <= 5:
                # if Fish.age is less than 3 - need to use fish.age to use the int value
                correct_ages2.append(bears)
                # add this element to the new list - use object type here
        self.bears = correct_ages2
        return None

    def bears_eating(self) -> None:
        """Updates eating method and removes fish."""
        for bear in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                bear.eat(3)  # this bear specifically eats 3
        return None

    def check_hunger(self) -> None:
        """Removes dead bears with a hunger score of 0."""
        living_bears: list[Bear] = []
        for bear in self.bears:
            if (
                bear.hunger_score != 0
            ):  # really means Bear() at this index, hunger_score
                living_bears.append(bear)
        self.bears = living_bears
        return None

    def repopulate_fish(self) -> None:
        """Adds baby fish to the list."""
        n: int = len(self.fish)
        baby_fish: int = (n // 2) * 4
        count: int = 0
        while count < baby_fish:
            self.fish.append(Fish())
            count += 1
        return None

    def repopulate_bears(self) -> None:
        """Adds baby bears to the list."""
        n: int = len(self.bears)
        baby_bears: int = n // 2
        count: int = 0
        while count < baby_bears:
            self.bears.append(Bear())
            count += 1
        return None

    def view_river(self) -> None:
        """Allows us to view the populations of the fish and bears."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return None

    def one_river_week(self) -> None:
        """Simulates one week of life in the river."""
        for _ in range(0, 7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Removes a certain number of fish from the list of fish."""
        # for idx in range(0, amount):
        count: int = 0
        while count < amount:
            self.fish.pop(0)
            count += 1
