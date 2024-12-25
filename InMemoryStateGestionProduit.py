from InMemorySateLog import InMemorySateLog
from InMemoryState import InMemoryState
from InMemoryStateAfficherProduit import InMemoryStateAfficherProduit
from InMemoryStateCreerProduit import InMemoryStateCreerProduit
from InMemoryStateUpdateProduit import InMemoryStateUpdateProduit


class InMemoryStateGestionProduit(InMemoryState):
    def __init__(self):
        super().__init__()

    def afficher_menu_gestion_produit(self):
        print("=" * 40)
        print("  APPLICATION GESTION.CO - GESTION PRODUITS")
        print("=" * 40)
        print("1. Ajouter un produit (Create)")
        print("2. Afficher les produits (Read)")
        print("3. Mettre à jour un produit (Update)")
        print("4. Supprimer un produit (Delete)")
        print("5. Retour au menu principal")
        print("=" * 40)
        choix = input("Veuillez choisir une option (1-5) -> ")
        return choix

    def active(self, session):
        while True:
            choix = self.afficher_menu_gestion_produit()
            if choix == "1":
                print("\nVous avez choisi : Ajouter un produit.\n")
                # Logique pour ajouter un produit
                session.setState(InMemoryStateCreerProduit())
                session.start()
            elif choix == "2":
                print("\nVous avez choisi : Afficher les produits.\n")
                # Logique pour afficher les produits
                session.setState(InMemoryStateAfficherProduit())
                session.start()
            elif choix == "3":
                print("\nVous avez choisi : Mettre à jour un produit.\n")
                # Logique pour mettre à jour un produit
                session.setState(InMemoryStateUpdateProduit())
                session.start()
            elif choix == "4":
                print("\nVous avez choisi : Supprimer un produit.\n")
                # Logique pour supprimer un produit
                id = int(input("Veuillez entrer l ID d un produit -> "))
                if not session.getProduitRepository().removeProduit(id):
                    print("\nProduit Introuvable.\n")
                session.setState(InMemorySateLog())
                session.start()
            elif choix == "5":
                print("Retour au menu principal.")
                break
            else:
                print("Choix invalide, veuillez réessayer.")


