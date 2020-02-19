class Pokemon:
    def __init__(self, name, level, type, max_hp, current_hp, is_knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.is_knocked_out = is_knocked_out


    def lose_health(self, amount):
        self.current_hp -= amount
        if self.current_hp < 0:
            self.knock_out()
            self.current_hp == 0
        else:
            print("{name} has lost {amount} HP and now has {current_hp} HP"\
            .format(name = self.name, amount = amount, current_hp = self.current_hp))


    def add_health(self, amount):
        #self.current_hp += amount
        if self.current_hp + amount > self.max_hp:
            amount = self.max_hp - self.current_hp
            self.current_hp = self.max_hp
        else:
            self.current_hp += amount
        print("{name} has gain {amount} HP and now has {current_hp} HP"\
        .format(name = self.name, amount = amount, current_hp = self.current_hp))


    def knock_out(self):
        self.is_knocked_out = True
        print("{name} has been knocked out".format(name = self.name))


    def revive(self):
        self.is_knocked_out = False
        print("{name} has been revived".format(name = self.name))

charmander = Pokemon("Charmander", 100, "Fire", 100, 100, False)
charmander.lose_health(30)
charmander.add_health(50)
#charmander.knock_out()
