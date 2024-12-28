from Gestion_stock.Exception.IdExistantException import IdExistantException
from Gestion_stock.Exception.IdIntrouvableException import IdIntrouvableException


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
        vente.setPrice(self.produitRepository.getProduitById(vente.getIdProduit()).getPrixUnitaire() * vente.getQuantite())

        self.venteRepository.verifyVente(vente)

        if self.venteRepository.getVenteById(vente.getIdVente()):
            raise IdExistantException(f"La vente avec l' ID {vente.getIdVente()} existe deja")

        if self.produitRepository.getProduitById(vente.getIdProduit()) is None:
            raise IdIntrouvableException(f"Le produit de la vente avec l' ID {vente.getIdProduit()} n'existe pas")

        self.produitRepository.vendreUnProduits(vente.getIdProduit(),vente.getQuantite())

        self.venteRepository.addVente(vente)

    def updateVente(self,vente):
        vente.setPrice(self.produitRepository.getProduitById(vente.getIdProduit()).getPrixUnitaire() * vente.getQuantite())
        produit = self.produitRepository.getProduitById(vente.getIdProduit())
        las_vente_quantite = self.venteRepository.getVenteById(vente.getIdVente()).getQuantite()

        if produit is None:
            raise IdIntrouvableException(f"Le produit ID {vente.getIdProduit()} de la vente n'existe pas")

        self.venteRepository.verifyVente(vente)

        if not self.venteRepository.removeVente(vente.getIdVente()):
            raise IdIntrouvableException(f"La vente id - {vente.getIdVente()} n'existe pas")

        produit.setQuantite((las_vente_quantite - vente.getQuantite())+produit.getQuantite())

        self.venteRepository.addVente(vente)


    def supprimerVente(self,vente):
        produit = self.produitRepository.getProduitById(vente.getIdProduit())
        produit.setQuantite(produit.getQuantite()+vente.getQuantite())
        self.venteRepository.removeVente(vente.getIdVente())


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


