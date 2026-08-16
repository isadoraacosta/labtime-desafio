from abc import ABC, abstractmethod

class EnergyObserver(ABC):
    @abstractmethod
    def update(self, energy):
        pass