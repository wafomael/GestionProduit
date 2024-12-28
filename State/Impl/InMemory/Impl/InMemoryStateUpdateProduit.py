from datetime import datetime

from Gestion_stock.Exception.IdExistantException import IdExistantException
from Gestion_stock.Exception.QuantiteInsufisanteException import QuantiteInsufisanteException
from Gestion_stock.State.Impl.InMemory.Impl.InMemorySateLog import InMemorySateLog
from Gestion_stock.State.Impl.InMemory.InMemoryState import InMemoryState
from Gestion_stock.Produit import Produit
from Gestion_stock.Exception.IdIntrouvableException import IdIntrouvableException


class InMemoryStateUpdateProduit(InMemoryState):
    def __init__(self):
        super().__init__()

    def active(self, session):
        produit = self.creer_produit()
        try:
            session.getProduitRepository().updateProduit(produit)
        except IdExistantException as e:
            print(f"\n{e}\n")
        except QuantiteInsufisanteException as e:
            print(f"\n{e}\n")
        except IdIntrouvableException as e:
            print(e)
        except Exception as e:
            print(f"\n{e}\n")

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
            typeId = input("Entrez l'id du type de produit : ")

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
            produit = Produit(idProduit, nom, quantite, prixUnitaire, typeId,isperisable, datePremption)
            return produit

        except ValueError as e:
            print(f"Erreur de saisie : {e}. Veuillez réessayer.")
            return self.creer_produit()

