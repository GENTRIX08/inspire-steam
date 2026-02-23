#Name : Gentrix Anyango
# Date : 19/02/2026
# Classes(objects) in python

class human:
    # First we define the attributes of a human being
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Nairobi"


    # We then create a constructor for the class object
    # The constructor will be used to create copies of this object
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello I am {self.human_name} Here is a story")
        print("There was once a bot that said hello world")

Amani = human("Amani", 17)
Harper = human("Harper", 26)    

# Let the humans created do things
Amani.tell_story()
print("Amani's_age is:", Amani.human_age)

# Modify one of the objects, without modifying other objects
Harper.city = "Kiambu"

print("Harper's location: ", Harper.city)
print("Amani's location: ", Amani.city)


class FighterCharacter:

    def __init__ (self, role, health, damage, speed):
        self.character_role = role
        self.character_health = health
        self.character_damage = damage
        self.character_speed = speed
    
    def run(self, direction):
        print(f"Game log: {self.character_role} runs {direction} at speed {self.character_speed}")
    
    def report_status(self):
        print(f"\nCharacter Log: \n Role: {self.character_role} \n Health: {self.character_health} \n Damage: {self.character_damage} \n Speed: {self.character_speed}\n ___ \n")
    
    def kick(self, opponent):

        character_damage = self.character_damage
        opponent.character_health = opponent.character_health - character_damage
        print(f"Game Log: {self.character_role} deals a damage of {character_damage} to the {opponent.character_role}.")
    
    def takle(self, opponent):
        # implement this so that the opponent's charater_speed is reduced by the damager dealt by the fighter
        # For instance, if the ninja's speed is 120, a takle from the warrior should reduce their speed to 80
        # Remember to remove the pass below before running your trial
        pass
        


ninja_character = FighterCharacter("Ninja", health=100, damage=40, speed=120)
warrior_character = FighterCharacter("warrior", health=160, damage=80, speed=80)


ninja_character.report_status()
warrior_character.report_status()

ninja_character.run("Up")
ninja_character.kick(warrior_character)

ninja_character.report_status()
warrior_character.report_status()
