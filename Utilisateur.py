class Utilisateur:
    def __init__(self, nom_utilisateur):
        self.nom_utilisateur = nom_utilisateur

    def getNomUtilisateur(self):
        return self.nom_utilisateur

    def __str__(self):
        return f"Utilisateur : {self.nom_utilisateur}"

