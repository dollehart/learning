class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} the {self.species} makes a sound.")

    def info(self):
        print(f"This is {self.name}. It's a {self.species}.")

# Example of usage:
my_animal = Animal("Buddy", "Dog")
my_animal.info()  # Output: This is Buddy. It's a Dog.
my_animal.make_sound()  # Output: Buddy the Dog makes a sound.
