from datetime import date


class Vente:
    def __init__(self,idVente,idProduit,quantite,dateResemption=date.today()):
        self.idVente = idVente
        self.idProduit = idProduit
        self.quantite = quantite
        self.dateResemption = dateResemption
        self.price = 0

    def getIdVente(self):
        return self.idVente
    def getIdProduit(self):
        return self.idProduit
    def getQuantite(self):
        return self.quantite
    def getDateResemption(self):
        return self.dateResemption
    def getPrice(self):
        return self.price

    def setPrice(self,price):
        self.price = price

    def __str__(self):
        return f"Vente {self.idVente}, Produit {self.idProduit}, Quantite {self.quantite}, Resemption {self.dateResemption}, Price : {self.getPrice()} $"

