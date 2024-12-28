from datetime import date, datetime

from Gestion_stock.Exception.IdExistantException import IdExistantException
from Gestion_stock.Exception.IdIntrouvableException import IdIntrouvableException
from Gestion_stock.Exception.QuantiteInsufisanteException import QuantiteInsufisanteException
from Gestion_stock.State.Impl.InMemory.Impl.InMemorySateLog import InMemorySateLog
from Gestion_stock.Vente import Vente
from Gestion_stock.State.Impl.InMemory.InMemoryState import InMemoryState

class InMemoryStateVendreProduit(InMemoryState):
    def __init__(self):
        super().__init__()

    def active(self, session):
        print("=" * 50)
        print("  CRÉATION D'UNE NOUVELLE VENTE")
        print("=" * 50)
        idVente = int(input("Entrez l'ID de la vente : "))

        idProduit = int(input("Entrez l'ID du produit : "))

        quantite = int(input("Entrez la quantité : "))

        choix_date = input("Voulez-vous spécifier une date de récemption ? (o/n) : ").strip().lower()

        dateR = date.today()

        if choix_date == 'o':
            dateResemption = input("Entrez la date de récemption (format AAAA-MM-JJ) : ")
            try:
                dateR = datetime.strptime(dateResemption, "%Y-%m-%d").date()
            except ValueError:
                dateR = date.today()
                print("\nFormat de date invalide. La date de péremption sera définie sur la date du jour.\n")

        vente = Vente(idVente, idProduit, quantite, dateR)

        try:
            session.vendreProduits(vente)
            print("Vente créée avec succès !")
            print(vente)
        except IdExistantException as e:
            print(f"\n{e}\n")
        except QuantiteInsufisanteException as e:
            print(f"\n{e}\n")
        except IdIntrouvableException as e:
            print(f"\n{e}\n")
        except Exception as e:
            print(f"\n{e}\n")


        session.setState(InMemorySateLog())
        session.start()


