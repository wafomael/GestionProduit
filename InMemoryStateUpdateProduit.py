from datetime import datetime

from InMemorySateLog import InMemorySateLog
from InMemoryState import InMemoryState
from Produit import Produit
from ProduitIntrouvableException import ProduitIntrouvableException


class InMemoryStateUpdateProduit(InMemoryState):
    def __init__(self):
        super().__init__()

    def active(self, session):
        produit = self.creer_produit()
        try:
            session.getProduitRepository().updateProduit(produit)
        except ProduitIntrouvableException as e:
            print(e)

        session.setState(InMemorySateLog())
        session.start()

    def creer_produit(self):
        print("=== Modification d'un Produit ===")
        try:
            # Demander les attributs nécessaires
            idProduit = int(input("Entrez l'ID du produit : "))
            nom = input("Entrez le nouveaux nom du produit : ").strip()
            quantite = int(input("Entrez la nouvelle quantité : "))
            prixUnitaire = float(input("Entrez le nouveaux prix unitaire : "))

            # Gestion de l'attribut optionnel 'isperisable'
            isperisable_input = input("Le produit est-il périssable ? (o/n) : ").strip().lower()
            isperisable = isperisable_input == 'o'

            # Gestion de l'attribut optionnel 'datePremption'
            datePremption = None
            if isperisable:
                date_input = input("Entrez la nouvelle date de péremption (format AAAA-MM-JJ) : ").strip()
                try:
                    datePremption = datetime.strptime(date_input, "%Y-%m-%d").date()
                except ValueError:
                    print("Format de date invalide. La date de péremption sera définie sur None.")

            # Création de l'objet Produit
            produit = Produit(idProduit, nom, quantite, prixUnitaire, isperisable, datePremption)
            return produit

        except ValueError as e:
            print(f"Erreur de saisie : {e}. Veuillez réessayer.")
            return self.creer_produit()

