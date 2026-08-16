from abc import ABC, abstractmethod


class Weapon(ABC):

    @abstractmethod
    def shoot(self):
        pass