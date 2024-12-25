class ProduitIntrouvableException(Exception):
    def __init__(self, message):
        self.messageException = f"ERREUR PRODUIT [{message}]"
        super().__init__(self.messageException)

    def __str__(self):
        return self.messageException
