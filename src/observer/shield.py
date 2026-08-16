from observer.observer import EnergyObserver

class Shield(EnergyObserver):
    def update(self, energy):
        if energy < 20:
            print("Escudos em modo de contigência!")