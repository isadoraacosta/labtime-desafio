"""
CrewMember

Representa um tripulante da nave.

O comportamento do tripulante pode ser alterado dinamicamente durante
a execução do programa.

Padrão utilizado: State.

"""

class CrewMember:

    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def work(self):
        self.state.work()
    