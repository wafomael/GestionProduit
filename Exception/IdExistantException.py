class IdExistantException(Exception):
    def __init__(self, message):
        self.messageException = f"ERREUR ID EXISTANT [{message}]"
        super().__init__(self.messageException)

    def __str__(self):
        return self.messageException
