from datetime import date

from VenteIntrouvableException import VenteIntrouvableException
from VenteRepository import VenteRepository

class InMemoryVenteRepository(VenteRepository):
    def __init__(self,ventes):
        super().__init__(ventes)

    def getAllVentes(self):
        return self.ventes

    def getVenteById(self, id):
        for vente in self.ventes:
            if vente.getIdVente() == id:
                return vente

    def getVenteByProductId(self, productId):
        venteByProduit = []
        for vente in self.ventes:
            if vente.getIdProduit() == productId:
                venteByProduit.append(vente)
        return venteByProduit

    def getRecuperedVente(self):
        recuperedVente = []
        for vente in self.ventes:
            if vente.getDateResemption() <= date.today():
                recuperedVente.append(vente)
        return recuperedVente

    def getUnRecuperedVente(self):
        unRecuperedVente = []
        for vente in self.ventes:
            if vente.getDateResemption() > date.today():
                unRecuperedVente.append(vente)
        return unRecuperedVente

    def addVente(self, vente):
        self.ventes.append(vente)

    def removeVente(self, id):
        for v in self.ventes:
            if v.getIdVente() == id:
                self.ventes.remove(v)
                return True

    def updateVente(self, vente):

        if not self.removeVente(vente.getIdVente()):
            raise VenteIntrouvableException(f"La vente id - {vente.getIdVente()}] n'existe pas")
        self.addVente(vente)





