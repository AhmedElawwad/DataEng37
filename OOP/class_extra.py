class Bird:

    def __init__(self, species, colour, can_fly=True):
        self.species = species
        self.colour = colour
        self.can_fly = can_fly
        self._age = 0

    def reproduce(self):
        if self._age< 2:
            return "Too young"
        return "Egg"

    def age_up(self, year=1):
        self._age += year

    def get_age(self):
        return self._age

class Penguin(Bird):

    def __init__(self, subspecies, colour= ("Black", "white")):
        super().__init__("Penguine", colour, can_fly=False)

    def hunt_for_fish(self):
        print("Splash")

class EmperorPenguin(Penguin):
    def __init__(self, subspecies, colour):
        self.species = subspecies
        self.colour = ["Blue", "white"]
        super().__init__(self,subspecies, colour )

