from datetime import date

from ProduitRepository import ProduitRepository
from QuantiteInsufisanteException import QuantiteInsufisanteException
from ProduitIntrouvableException import ProduitIntrouvableException


class InMemoryProduitRepository(ProduitRepository):
    def __init__(self,produits):
        super().__init__(produits)

    def getAllProduits(self):
        return self.Produits

    def getProduitById(self, idProduit):
        for produit in self.Produits:
            if produit.getIdProduit() == idProduit:
                return produit

    def getProduitByName(self, name):
        for produit in self.Produits:
            if produit.getNom() == name:
                return produit

    def getPerisableProduits(self):
        perisableProduits = []
        for produit in self.Produits:
            if produit.getIsperisable():
                perisableProduits.append(produit)

        return perisableProduits

    def getUnPerisableProduits(self):
        unPerisableProduits = []
        for produit in self.Produits:
            if not produit.getIsperisable():
                unPerisableProduits.append(produit)

        return unPerisableProduits

    def getPerisedProduits(self):
        perisedProduits = []
        for produit in self.Produits:
            if produit.getDatePremption() is not None and produit.getDatePremption() < date.today():
                perisedProduits.append(produit)

        return perisedProduits

    def vendreUnProduits(self,idProduit,quantite):
        produit = self.getProduitById(idProduit)
        quantite_produit = produit.getQuantite()

        if quantite_produit < quantite:
            raise QuantiteInsufisanteException(f"la quantite={quantite} du produit [{produit.getNom()} id - {produit.getIdProduit()}] est insufusante")


        produit.setQuantite(quantite_produit-quantite)

    def addProduit(self,produit):
        self.Produits.append(produit)

    def removeProduit(self,idProduit):
        for p in self.Produits:
            if p.getIdProduit() == idProduit:
                self.Produits.remove(p)
                return True
        return False

    def updateProduit(self,produit):
        if not self.removeProduit(produit.getIdProduit()):
            raise ProduitIntrouvableException(f"Le produit [{produit.getNom()} id - {produit.getIdProduit()}] n'existe pas")
        self.addProduit(produit)

