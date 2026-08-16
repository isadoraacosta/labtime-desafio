class CrewMember:

    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def work(self):
        self.state.work()
    