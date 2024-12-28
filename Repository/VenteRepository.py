from abc import ABC, abstractmethod

class VenteRepository(ABC):
    def __init__(self, ventes):
        self.ventes = ventes

    @abstractmethod
    def getAllVentes(self):
        pass
    @abstractmethod
    def getVenteById(self, id):
        pass
    @abstractmethod
    def getVenteByProductId(self, productId):
        pass

    @abstractmethod
    def getRecuperedVente(self):
        pass

    @abstractmethod
    def getRecuperedVente(self):
        pass

    @abstractmethod
    def getUnRecuperedVente(self):
        pass

    @abstractmethod
    def addVente(self, vente):
        pass
    @abstractmethod
    def removeVente(self, id):
        pass
    @abstractmethod
    def updateVente(self, vente):
        pass

    @abstractmethod
    def getVentesByPriceAscending(self):
        pass

    @abstractmethod
    def getVentesByPriceDescending(self):
        pass

    @abstractmethod
    def verifyVente(self, vente):
        pass

