from Gestion_stock.State.Impl.InMemory.Impl.InMemorySateLog import InMemorySateLog
from Gestion_stock.State.Impl.InMemory.Impl.InMemoryStateUpdateVente import InMemoryStateUpdateVente
from Gestion_stock.State.Impl.InMemory.Impl.InMemoryStateAfficherVente import InMemoryStateAfficherVente
from Gestion_stock.State.Impl.InMemory.Impl.InMemoryStateVendreProduit import InMemoryStateVendreProduit
from Gestion_stock.State.Impl.InMemory.InMemoryState import InMemoryState

class InMemoryStateGestionVente(InMemoryState):
    def __init__(self):
        super().__init__()

    def active(self, session):
        while True:
            choix = self.afficher_menu_vente()
            if choix == "1":
                print("\nVous avez choisi : Effectuer une vente.\n")
                # Logique pour effectuer une vente
                session.setState(InMemoryStateVendreProduit())
                session.start()
                break
            elif choix == "2":
                print("\nVous avez choisi : Afficher les ventes.\n")
                # Logique pour afficher toutes les ventes
                session.setState(InMemoryStateAfficherVente())
                session.start()
                break
            elif choix == "3":
                print("\nVous avez choisi : Modifier une vente.\n")
                # Logique pour modifier une vente
                session.setState(InMemoryStateUpdateVente())
                session.start()
                break
            elif choix == "4":
                print("\nVous avez choisi : Supprimer une vente.\n")
                # Logique pour supprimer une vente
                id = int(input("Entrer l id de la vente : "))
                vente = session.getVenteRepository().getVenteById(id)
                session.supprimerVente(vente)

                session.setState(InMemorySateLog())
                session.start()
                break
            elif choix == "5":
                print("\nRetour au menu principal.\n")
                session.setState(InMemorySateLog())
                session.start()
                break
            else:
                print("\nChoix invalide, veuillez réessayer.\n")

    def afficher_menu_vente(self):
        print("=" * 50)
        print("  APPLICATION GESTION.CO - GESTION DES VENTES")
        print("=" * 50)
        print("Option 1 : Effectuer une vente.")
        print("Option 2 : Afficher les ventes.")
        print("Option 3 : Modifier une vente.")
        print("Option 4 : Supprimer une vente.")
        print("Option 5 : Retour au menu principal.")
        print("=" * 50)
        choix = input("Veuillez choisir une option (1-5) : ")
        return choix
