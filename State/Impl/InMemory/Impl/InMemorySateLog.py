from Gestion_stock.State.Impl.InMemory.InMemoryState import InMemoryState

class InMemorySateLog(InMemoryState):
    def __init__(self):
        super().__init__()

    def active(self, session):
        from Gestion_stock.State.Impl.InMemory.Impl.InMemoryStateMenue import InMemoryStateMenue
        print("active")

        session.setState(InMemoryStateMenue())
        session.start()


