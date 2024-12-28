from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def active(self,session):
        pass