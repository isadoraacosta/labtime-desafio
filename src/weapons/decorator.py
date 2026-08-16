"""
WeaponDecorator

Classe base dos modificadores das armas.

Permite adicionar novas funcionalidades sem modificar
a implementação original.

Padrão utilizado: Decorator.

"""

from weapons.weapon import Weapon

class WeaponDecorator(Weapon):

    def __init__(self, weapon):
        self.weapon = weapon