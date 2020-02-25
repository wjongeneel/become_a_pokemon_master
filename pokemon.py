# This class represents a pokemon
class Pokemon:
    def __init__(self, name, level, type, max_hp, current_hp, is_knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.is_knocked_out = is_knocked_out


    def lose_health(self, amount):
        if amount >= self.current_hp: # Condition that checks if the amount of damage is greater than the current_hp, if so, amount is current_hp
            amount = self.current_hp
            self.current_hp -= amount
            print("{name} has lost {amount} HP and now has {current_hp} HP".format(name = self.name, amount = amount, current_hp = self.current_hp))
            self.knock_out()
        else: # If current_hp is greater than the ammount
            self.current_hp -= amount
            print("{name} has lost {amount} HP and now has {current_hp} HP".format(name = self.name, amount = amount, current_hp = self.current_hp))


    def add_health(self, amount):
        #self.current_hp += amount
        if self.current_hp + amount >= self.max_hp:
            amount = self.max_hp - self.current_hp
            self.current_hp = self.max_hp
        else:
            self.current_hp += amount
        print("{name} has gain {amount} HP and now has {current_hp} HP".format(name = self.name, amount = amount, current_hp = self.current_hp))


    def knock_out(self):
        self.is_knocked_out = True
        print("{name} has been knocked out".format(name = self.name))


    def revive(self):
        self.is_knocked_out = False
        print("{name} has been revived".format(name = self.name))


    def attack(self, pokemon):
        if pokemon.is_knocked_out == False:
            base_damage = self.level
            # the statements below check whether the attacking pokemon has an attacking advantage or disadvantage
            if self.type == "Fire" and pokemon.type == "Grass":
                damage = base_damage * 2
            elif self.type == "Fire" and pokemon.type == "Water":
                damage = base_damage * 0.5
            elif self.type == "Fire" and pokemon.type == "Fire":
                damage = base_damage * 0.5
            elif self.type == "Water" and pokemon.type == "Grass":
                damage = base_damage * 0.5
            elif self.type == "Water" and pokemon.type == "Water":
                damage = base_damage * 0.5
            elif self.type == "Water" and pokemon.type == "Fire":
                damage = base_damage * 2
            if self.type == "Grass" and pokemon.type == "Grass":
                damage = base_damage * 0.5
            elif self.type == "Grass" and pokemon.type == "Water":
                damage = base_damage * 2
            elif self.type == "Grass" and pokemon.type == "Fire":
                damage = base_damage * 0.5
            print("{self_name} attacks {pokemon_name}!".format(self_name = self.name, pokemon_name = pokemon.name))
            pokemon.lose_health(damage)
        else:
            print("{self_name} attacks {pokemon_name}!".format(self_name = self.name, pokemon_name = pokemon.name))
            print("You cannot attack a pokemon that has been knocked out!")


class Trainer:
    def __init__(self, pokemon_list, name, number_of_potions, current_active_pokemon):
        self.pokemon_list = pokemon_list
        self.name = name
        self.number_of_potions = number_of_potions
        self.current_active_pokemon = pokemon_list[0]


    def use_potion(self):
        self.current_active_pokemon.add_health(50)
        print("{trainer_name} uses a potion on {pokemon_name}.".format(trainer_name = self.name, pokemon_name = self.current_active_pokemon.name))


    def attack_trainer(self, trainer):
        self.current_active_pokemon.attack(trainer.current_active_pokemon)


    def switch_pokemon(self, pokemon_name):
        pokemon_exists = False
        for i in range(0, len(self.pokemon_list)):
            if (pokemon_name == self.current_active_pokemon.name):
                print("{trainer_name} tries to switch to {pokemon}, but failed. {pokemon} is already active!".format(trainer_name = self.name, pokemon = pokemon_name))
                pokemon_exists = True
                break
            elif (pokemon_name == self.pokemon_list[i].name) and (self.pokemon_list[i].is_knocked_out !=True):
                self.current_active_pokemon = self.pokemon_list[i]
                print("{trainer_name} switches pokemon to {pokemon}!".format(trainer_name = self.name, pokemon = self.current_active_pokemon.name))
                pokemon_exists = True
                break
            elif (pokemon_name == self.pokemon_list[i].name) and (self.pokemon_list[i].is_knocked_out == True):
                print("{trainer_name} tries to switch to {pokemon}, but failed. You cannot switch to knocked out pokemon!".format(trainer_name = self.name, pokemon = self.pokemon_list[i].name))
                pokemon_exitst = True
                break
        if pokemon_exists == False:
            print("{trainer_name} tries to switch to {pokemon}, but failed. There is no pokemon with that name in the pokemon list".format(trainer_name = self.name, pokemon = pokemon_name))
