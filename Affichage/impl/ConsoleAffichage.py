from Gestion_stock.Affichage.Affichage import Affichage

class ConsoleAffichage(Affichage):
    def __init__(self):
        super().__init__()

    def afficherProduit(self,produits):
        entete = f"{'ID':<10}{'Nom':<20}{'Quantité':<10}{'Prix Unitaire ($)':<20}{'Type de produit':<20}{'Périssable':<15}{'Date Péremption':<20}"
        print(entete)
        print("-" * len(entete))

        for produit in produits:
            if produit == None:
                print("Produit(s) Introuvable ou inexistant")
            else:
                idProduit = produit.getIdProduit()
                nom = produit.getNom()
                quantite = produit.getQuantite()
                prixUnitaire = produit.getPrixUnitaire()
                isperisable = "Oui" if produit.getIsperisable() else "Non"
                datePremption = produit.getDatePremption() or "Aucune"
                typeProduit = produit.getTypeProduit()
                print(f"{idProduit:<10}{nom:<20}{quantite:<10}{prixUnitaire:<20}{typeProduit:<20}{isperisable:<15}{str(datePremption):<20}")

    def afficherVente(self,ventes):
        # Entête du tableau
        header = f"{'ID Vente':<10} {'ID Produit':<12} {'Quantité':<10} {'Date Resemption':<15} {'Prix ($)':<10}"
        print(header)
        print("-" * len(header))


        # Lignes du tableau
        for vente in ventes:
            if vente == None:
                print("Vente(s) Introuvable ou inexistant")
            else:
                print(f"{vente.getIdVente():<10} {vente.getIdProduit():<12} {vente.getQuantite():<10} {str(vente.getDateResemption()):<15} {vente.getPrice():<10.2f}")

