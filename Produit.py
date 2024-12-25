from datetime import date


class Produit:
    def __init__(self,idProduit, nom, quantite,prixUnitaire, isperisable=False,datePremption =None):
        self.idProduit = idProduit
        self.nom = nom
        self.quantite = quantite
        self.prixUnitaire = prixUnitaire
        self.isperisable = isperisable
        self.datePremption = datePremption

    def getIdProduit(self):
        return self.idProduit
    def getNom(self):
        return self.nom
    def getQuantite(self):
        return self.quantite
    def getIsperisable(self):
        return self.isperisable
    def getDatePremption(self):
        return self.datePremption
    def getPrixUnitaire(self):
        return self.prixUnitaire

    def setDatePremption(self, datePremption):
        self.datePremption = datePremption
        self.isperisable = True

    def setQuantite(self, quantite):
        self.quantite = quantite

    def __str__(self):
        return f"Produit {self.idProduit} : {self.nom}, Quantite {self.quantite} : {self.prixUnitaire} $ date pereption {self.datePremption}"


