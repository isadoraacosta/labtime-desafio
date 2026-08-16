from observer.observer import EnergyObserver

class Lights(EnergyObserver):
   
    def update(self, energy):
        if energy < 20:
            print("Luzes desligadas!")