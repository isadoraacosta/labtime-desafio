class EnergyCore:
    def __init__(self):
        self.energy = 100
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.energy) 

    def reduce_energy(self, amount):
        self.energy -= amount
        print(f"Energia atual: {self.energy}%")
        self.notify()   

    def take_damage(self, damage):
    print(f"A nave sofreu {damage} de dano.")
    self.reduce_energy(damage)