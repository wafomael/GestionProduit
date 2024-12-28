from abc import ABC, abstractmethod

class Affichage(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def afficherProduit(self,produits):
        pass
    @abstractmethod
    def afficherVente(self,ventes):
        pass
