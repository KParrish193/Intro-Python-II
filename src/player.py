# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__ (self, name, description, location, hp, attack, defense, itembag, equipment):
        self.name = name
        self.description = description
        self.location = location
        self.itembag = itembag
        self.equipment = equipment
        self.hp = hp
        self.defense = defense
        self.attack = attack

def move_to(self, direction, current_location):
    # ? move in the specified direction
    attribute = direction + 'to'
    # ? can we move that direction : yes
    if hasattr(current_location, attribute):
        #? get room in specified direction
        return getattr(current_location, attribute)
    # ? can we move that direction : no
    print("You can't move that way\n")
    return(current_location)

