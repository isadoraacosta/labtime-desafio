
"""
Weapon

Interface responsável por definir o comportamento básico
de todas as armas.

Padrão utilizado: Decorator.

"""

from abc import ABC, abstractmethod


class Weapon(ABC):

    @abstractmethod
    def shoot(self):
        pass