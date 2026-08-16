"""
EnergyObserver

Interface utilizada pelos sistemas que precisam ser notificados quando
a energia da nave é alterada.

Padrão utilizado: Observer.

"""

from abc import ABC, abstractmethod

class EnergyObserver(ABC):
    @abstractmethod
    def update(self, energy):
        pass