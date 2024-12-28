from Gestion_stock.Affichage.impl.ConsoleAffichage import ConsoleAffichage
from Gestion_stock.State.Impl.InMemory.Impl.InMemorySateLog import InMemorySateLog
from Gestion_stock.State.Impl.InMemory.InMemoryState import InMemoryState

class InMemoryStateAfficherVente(InMemoryState):
    def __init__(self):
        super().__init__()
        self.consoleAfichage = ConsoleAffichage()

    def active(self,session):
        while True:
            choix = self.afficher_menu_affichage_ventes()
            if choix == "1":
                print("\nVous avez choisi : Afficher toutes les ventes.\n")
                # Logique pour afficher toutes les ventes
                self.consoleAfichage.afficherVente(session.getVenteRepository().getAllVentes())
            elif choix == "2":
                print("\nVous avez choisi : Afficher les ventes récupérées.\n")
                # Logique pour afficher les ventes récupérées
                self.consoleAfichage.afficherVente(session.getVenteRepository().getRecuperedVente())
            elif choix == "3":
                print("\nVous avez choisi : Afficher les ventes non récupérées.\n")
                # Logique pour afficher les ventes non récupérées
                self.consoleAfichage.afficherVente(session.getVenteRepository().getUnRecuperedVente())
            elif choix == "4":
                print("\nVous avez choisi : Afficher les ventes par ordre croissant de date.\n")
                # Logique pour afficher les ventes par ordre croissant
                self.consoleAfichage.afficherVente(session.getVenteRepository().getVentesByPriceAscending())
            elif choix == "5":
                print("\nVous avez choisi : Afficher les ventes par ordre décroissant de date.\n")
                # Logique pour afficher les ventes par ordre décroissant
                self.consoleAfichage.afficherVente(session.getVenteRepository().getVentesByPriceDescending())
            elif choix == "6":
                print("\nVous avez choisi : Afficher une vente par son id.\n")
                # Logique pour afficher les produits épuisés
                id = int(input("Entrer l id de la vente : "))
                self.consoleAfichage.afficherVente([session.getVenteRepository().getVenteById(id)])
            elif choix == "7":
                print("\nVous avez choisi : Afficher une vente par son id de produit.\n")
                id = int(input("Entrer l id du produit de la vente : "))
                self.consoleAfichage.afficherVente(session.getVenteRepository().getVenteByProductId(id))
            elif choix == "8":
                print("\nRetour au menu principal.\n")
                session.setState(InMemorySateLog())
                session.start()
                break
            else:
                print("\nChoix invalide, veuillez réessayer.\n")


    def afficher_menu_affichage_ventes(self):
        print("=" * 50)
        print("  APPLICATION GESTION.CO - AFFICHAGE DES VENTES")
        print("=" * 50)
        print("Option 1 : Afficher toutes les ventes.")
        print("Option 2 : Afficher les ventes récupérées.")
        print("Option 3 : Afficher les ventes non récupérées.")
        print("Option 4 : Afficher les ventes par ordre croissant quantite.")
        print("Option 5 : Afficher les ventes par ordre décroissant de quantite.")
        print("Option 6 : Afficher une vente par son id.")
        print("Option 7 : Afficher une vente par son id de produit.")
        print("Option 8 : Retour au menu principal.")
        print("=" * 50)
        choix = input("Veuillez choisir une option (1-7) : ")
        return choix