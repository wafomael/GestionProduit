from datetime import date

from Gestion_stock.Exception.IdIntrouvableException import IdIntrouvableException
from Gestion_stock.Exception.QuantiteInsufisanteException import QuantiteInsufisanteException
from Gestion_stock.Repository.VenteRepository import VenteRepository

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
        venteByvente = []
        for vente in self.ventes:
            if vente.getIdvente() == productId:
                venteByvente.append(vente)
        return venteByvente

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
        self.verifyVente(vente)
        self.ventes.append(vente)

    def removeVente(self, id):
        for v in self.ventes:
            if v.getIdVente() == id:
                self.ventes.remove(v)
                return True

    def updateVente(self, vente):

        self.addVente(vente)

    def getVentesByPriceAscending(self):
        return sorted(self.ventes, key=lambda vente: vente.getQuantite())

    def getVentesByPriceDescending(self):
        return sorted(self.ventes, key=lambda vente: vente.getQuantite(), reverse=True)

    def verifyVente(self, vente):
        if vente.getQuantite() <= 0:
            raise QuantiteInsufisanteException(f"La quantite de produit de la vente doit etre superier a 0.")
        if vente.getPrice() <= 0:
            raise QuantiteInsufisanteException(f"Le prix de la vente doit etre superier a 0 $.")
        
    
    








