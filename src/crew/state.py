from abc import ABC, abstractmethod


class CrewState(ABC):

    @abstractmethod
    def work(self):
        pass