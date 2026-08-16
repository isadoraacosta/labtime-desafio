"""
Spaceship

Representa a nave espacial.

A nave pode equipar diferentes armas e receber modificadores
dinamicamente.

Padrão utilizado: Decorator.

"""


from weapons.weapon import Weapon

class Spaceship:

    def __init__(self):
        self.weapon = None

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def add_modifier(self, modifier):
        self.weapon = modifier(self.weapon) 

    def shoot(self):
        return self.weapon.shoot() if self.weapon else "Nenhuma arma equipada."