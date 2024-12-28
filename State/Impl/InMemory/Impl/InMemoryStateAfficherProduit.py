from Gestion_stock.State.Impl.InMemory.Impl.InMemorySateLog import InMemorySateLog
from Gestion_stock.State.Impl.InMemory.InMemoryState import InMemoryState
from Gestion_stock.Affichage.impl.ConsoleAffichage import ConsoleAffichage

class InMemoryStateAfficherProduit(InMemoryState):
    def __init__(self):
        super().__init__()
        self.consoleAffichage = ConsoleAffichage()

    def afficher_menu_affichage_produits(self):
        print("=" * 50)
        print("  APPLICATION GESTION.CO - AFFICHAGE DES PRODUITS")
        print("=" * 50)
        print("Option 1 : Affiche tous les produits.")
        print("Option 2 : Affiche un produit spécifique par son ID.")
        print("Option 3 : Affiche un produit par son nom.")
        print("Option 4 : Affiche tous les produits périssables.")
        print("Option 5 : Affiche les produits périmés (avec une date de péremption dépassée).")
        print("Option 6 : Affiche les produits non périssables.")
        print("Option 7 : Retour au menu principal.")
        print("=" * 50)
        choix = input("Veuillez choisir une option (1-7) -> ")
        return choix

    def active(self, session):
        while True:
            choix = self.afficher_menu_affichage_produits()
            if choix == "1":
                print("Vous avez choisi : Affiche tous les produits.")
                # Logique pour afficher tous les produits
                self.consoleAffichage.afficherProduit(session.getProduitRepository().getAllProduits())

                
            elif choix == "2":
                print("\nVous avez choisi : Affiche un produit spécifique par son ID.\n")
                # Logique pour afficher un produit par ID
                id = int(input("Veuillez entrer l ID d un produit -> "))
                self.consoleAffichage.afficherProduit([session.getProduitRepository().getProduitById(id)])
                
            elif choix == "3":
                print("\nVous avez choisi : Affiche un produit par son nom.\n")
                # Logique pour afficher un produit par nom
                nom = input("Veuillez entrer le nom du produit -> ")
                self.consoleAffichage.afficherProduit([session.getProduitRepository().getProduitByName(nom)])
                
            elif choix == "4":
                print("\nVous avez choisi : Affiche tous les produits périssables.\n")
                # Logique pour afficher tous les produits périssables
                self.consoleAffichage.afficherProduit(session.getProduitRepository().getPerisableProduits())
                
            elif choix == "5":
                print("\nVous avez choisi : Affiche les produits périmés.\n")
                # Logique pour afficher les produits périmés
                self.consoleAffichage.afficherProduit(session.getProduitRepository().getPerisedProduits())
                
            elif choix == "6":
                print("\nVous avez choisi : Affiche les produits non périssables.\n")
                # Logique pour afficher les produits non périssables
                self.consoleAffichage.afficherProduit(session.getProduitRepository().getUnPerisableProduits())
                
            elif choix == "7":
                print("\nRetour au menu principal.\n")
                session.setState(InMemorySateLog())
                session.start()
                break
            else:
                print("Choix invalide, veuillez réessayer.")

