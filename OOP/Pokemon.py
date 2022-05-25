class Pokemon:
    def __init__(self, name, type, hp, attack, defence):

        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.level = 1
        self.type = type
        self.moves = []


    def receive_attack(self, power, is_super_affective = False):

        if is_super_affective:
            self.hp -= (power - self.defence) * 1.5

        else:
            self.hp -= (power - self.defence)

    def level_up(self, levels = 1):

        self.level += levels
        self.hp += levels * 2
        self.attack += levels
        self.defence += levels





