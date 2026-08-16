"""
CrewState

Interface responsável por definir os comportamentos possíveis
de um tripulante.

Padrão utilizado: State.

"""

from abc import ABC, abstractmethod


class CrewState(ABC):

    @abstractmethod
    def work(self):
        pass