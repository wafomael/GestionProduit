from InMemoryState import InMemoryState
from InMemoryStateGestionProduit import InMemoryStateGestionProduit

class InMemoryStateMenue(InMemoryState):
    def __init__(self):
        super().__init__()

    def afficher_menu(self):
        print("=" * 30)
        print("  Application Gestion.co  ")
        print("=" * 30)
        print("1. Gérer les produits")
        print("2. Gérer les ventes")
        print("3. Statistiques")
        print("4. Quitter")
        print("=" * 30)

        # Saisir l'option choisie par l'utilisateur
        choix = input("Veuillez sélectionner une option (1-4) -> ")
        return choix

    def active(self,session):
        while True:
            choix = self.afficher_menu()

            if choix == "1":
                print("\nVous avez choisi : Gérer les produits\n")
                # Appeler une fonction pour gérer les produits
                session.setState(InMemoryStateGestionProduit())
                session.start()
            elif choix == "2":
                print("Vous avez choisi : Gérer les ventes")
                # Appeler une fonction pour gérer les ventes
            elif choix == "3":
                print("Vous avez choisi : Statistiques")
                # Appeler une fonction pour afficher les statistiques
            elif choix == "4":
                print("Au revoir!")
                break
            else:
                print("\nOption invalide. Veuillez réessayer.\n")





