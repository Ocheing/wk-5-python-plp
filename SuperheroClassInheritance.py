# Parent class - Superpower
class Superpower:
    def __init__(self, power_name):
        self.power_name = power_name
    
    def use_power(self):
        pass  

# Child class - Superhero (inherits from Superpower)
class Superhero(Superpower):
    def __init__(self, name, power_name, alter_ego):
        super().__init__(power_name) 
        self.name = name
        self.alter_ego = alter_ego

    def use_power(self):
        print(f"{self.name} uses {self.power_name}!")

    def display_info(self):
        print(f"Superhero Name: {self.name}")
        print(f"Alter Ego: {self.alter_ego}")
        print(f"Superpower: {self.power_name}")

# Create objects for different superheroes
hero1 = Superhero("Superman", "Super Strength", "Clark Kent")
hero2 = Superhero("Flash", "Super Speed", "Barry Allen")

# Display superhero info
hero1.display_info()
hero2.display_info()

# Use powers
hero1.use_power()
hero2.use_power()
