class Move:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

    def __repr__(self):
        return f"Move (name={self.name}, type={self.type}, power={self.power}"

    def __str__(self):
        return f"{self.name} {self.type} {self.power}"

flame_thorwer = Move(
    name="Flamethorwer",
    type="fire",
    power=100
)
