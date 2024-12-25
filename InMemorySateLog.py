from InMemoryState import InMemoryState

class InMemorySateLog(InMemoryState):
    def __init__(self):
        super().__init__()

    def active(self, session):
        from InMemoryStateMenue import InMemoryStateMenue
        print("active")

        session.setState(InMemoryStateMenue())
        session.start()


