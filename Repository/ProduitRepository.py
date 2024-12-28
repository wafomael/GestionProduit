from abc import ABC, abstractmethod

class ProduitRepository(ABC):
    def __init__(self,Produits):
        self.Produits = Produits

    @abstractmethod
    def getAllProduits(self):
        pass

    @abstractmethod
    def getProduitById(self,idProduit):
        pass

    @abstractmethod
    def getProduitByName(self,name):
        pass

    @abstractmethod
    def getPerisableProduits(self):
        pass

    def getUnPerisableProduits(self):
        pass

    @abstractmethod
    def getPerisedProduits(self):
        pass

    @abstractmethod
    def vendreUnProduits(self,idProduit,quantite):
        pass

    @abstractmethod
    def addProduit(self, produit):
        pass

    @abstractmethod
    def removeProduit(self, idProduit):
        pass

    @abstractmethod
    def updateProduit(self,produit):
        pass

    @abstractmethod
    def idIsExiste(self,idProduit):
        pass
    @abstractmethod
    def verifyProduit(self,produit):
        pass

