class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
hero_1 = SuperHero("Batman", "Intelligence", 100)
hero_2 = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(hero_1.name)
print(hero_1.power)
print(hero_1.health)
print(hero_2.name)
print(hero_2.power)
print(hero_2.health)