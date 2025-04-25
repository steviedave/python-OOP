# Base Class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.strength_level = strength_level
    
    def show_identity(self):
        return f"I am {self.name}, and I possess the power of {self.power}!"
    
    def fight_crime(self):
        return f"{self.name} is fighting crime with {self.power}! 💥"

# Subclass using inheritance
class TechHero(Superhero):
    def __init__(self, name, strength_level, gadgets):
        super().__init__(name, "Technology", strength_level)
        self.gadgets = gadgets
    
    def fight_crime(self):
        return f"{self.name} uses {', '.join(self.gadgets)} to outsmart villains! 🧠🤖"

# Example usage
hero1 = Superhero("StormStrike", "Lightning", 90)
hero2 = TechHero("CyberKnight", 80, ["Drone Swarm", "EMP Blaster"])

print(hero1.show_identity())
print(hero1.fight_crime())
print(hero2.show_identity())
print(hero2.fight_crime())
