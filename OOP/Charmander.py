from Pokemon import Pokemon
from move import Move

class Charmander(Pokemon):
    def __init__(self):
        super().__init__(
                         name="Charmander"
                         ,type="Fire"
                         ,hp =7
                         ,attack=9
                         ,defence=5
                         )
        self.moves.append(Move("Scratch", 'normal', 10))
        self.moves.append(Move("Growl", "Normal", 0))


    def use_move(self, move_name):
        """
        iterate through the move set
        check if the move name matches the name
        if yes use the move
        otherwise, keep looking
        """

        for move in self.moves:
            if move_name == move.name:
                print(f"{self.name} used {move.name}")
                return  move.power + self.attack, move.type




class Pickachu(Pokemon):

    def __init__(self):
        super().__init__("Pickachu", "Electric", hp = 6 )


char = Charmander()

print(char.type)
print(char.hp)
print(char.moves)

for move in char.moves:
    print(f"({move.name}) ({move.type}) ({move.power})")

power, move_type = char.use_move("Scratch")
print(power, type(power))
print(move_type, type(move_type))
print(char.moves)