from weapons.weapon import Weapon

class WeaponDecorator(Weapon):

    def __init__(self, weapon):
        self.weapon = weapon