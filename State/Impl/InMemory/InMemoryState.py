from Gestion_stock.State.State import State

class InMemoryState(State):
    def __init__(self):
        super().__init__()

    def active(self,session):
        pass

