from datetime import date

from Gestion_stock.Exception.IdExistantException import IdExistantException
from Gestion_stock.Repository.ProduitRepository import ProduitRepository
from Gestion_stock.Exception.QuantiteInsufisanteException import QuantiteInsufisanteException
from Gestion_stock.Exception.IdIntrouvableException import IdIntrouvableException


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
            raise QuantiteInsufisanteException(f"la quantite={quantite} du produit [{produit.getNom()} id - {produit.getIdProduit()}] est insufusante pour la vente")


        produit.setQuantite(quantite_produit-quantite)

    def idIsExiste(self,idProduit):
        for p in self.Produits:
            if idProduit == p.getIdProduit():
                return True
        return False

    def addProduit(self,produit):
        if self.idIsExiste(produit.getIdProduit()):
            raise IdExistantException(f"Id {produit.getIdProduit()} existe dejas")
        self.verifyProduit(produit)

        self.Produits.append(produit)

    def verifyProduit(self,produit):
        if produit.getQuantite() <= 0:
            raise QuantiteInsufisanteException(f"La quantite du produit doit etre superier a 0.")
        if produit.getPrixUnitaire() <= 0:
            raise QuantiteInsufisanteException(f"Le prix du produit doit etre superier a 0 $.")

    def removeProduit(self,idProduit):
        for p in self.Produits:
            if p.getIdProduit() == idProduit:
                self.Produits.remove(p)
                return True
        return False

    def updateProduit(self,produit):
        self.verifyProduit(produit)

        if not self.removeProduit(produit.getIdProduit()):
            raise IdIntrouvableException(f"Le produit [{produit.getNom()} id - {produit.getIdProduit()}] n'existe pas")

        self.Produits.append(produit)


    def idIsExiste(self, idProduit):
        for p in self.Produits:
            if p.getIdProduit() == idProduit:
                return True
        return False
