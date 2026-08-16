from observer.observer import EnergyObserver

class Panel(EnergyObserver):
   
    def update(self, energy):
        if energy < 20:
            print("Alerta de estado crítico!!")