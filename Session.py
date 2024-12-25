class Session:
    def __init__(self,utilisateur,venteRepository,produitRepository,state):
        self.utilisateur = utilisateur
        self.venteRepository = venteRepository
        self.produitRepository = produitRepository
        self.state = state

    def setState(self,state):
        self.state = state

    def start(self):
        self.state.active(self)

    def getVenteRepository(self):
        return self.venteRepository
    def getProduitRepository(self):
        return self.produitRepository

    def getProduit(self):
        return self.produitRepository.getAllProduits()

    def getVente(self):
        return self.venteRepository.getAllVentes()

    def vendreProduits(self,vente):
        self.produitRepository.vendreUnProduits(vente.getIdProduit(),vente.getQuantite())
        vente.setPrice(self.produitRepository.getProduitById(vente.getIdProduit()).getPrixUnitaire()*vente.getQuantite())
        self.venteRepository.addVente(vente)

    def ajoutProduit(self,produit):
        self.produitRepository.addProduit(produit)

    def supprimProduit(self,idproduit):
        self.produitRepository.removeProduit(idproduit)

    def misAjourProduit(self,produit):
        self.produitRepository.updateProduit(produit)

    def supprimVente(self,idvente):
        self.venteRepository.removeVente(idvente)

    def misAjourVente(self,vente):
        vente.setPrice(self.produitRepository.getProduitById(vente.getIdProduit()).getPrixUnitaire() * vente.getQuantite())
        self.venteRepository.updateVente(vente)


