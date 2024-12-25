from datetime import date

from ConsoleAffichage import ConsoleAffichage
from InMemoryStateMenue import InMemoryStateMenue
from ProduitIntrouvableException import ProduitIntrouvableException
from QuantiteInsufisanteException import QuantiteInsufisanteException
from InMemoryProduitRepository import InMemoryProduitRepository
from InMemoryVenteRepository import InMemoryVenteRepository
from Produit import Produit
from Utilisateur import Utilisateur
from Vente import Vente
from Session import Session

produit = InMemoryProduitRepository([])
vente = InMemoryVenteRepository([])

utilisateur = Utilisateur("franck")

state = InMemoryStateMenue()

session = Session(utilisateur,vente,produit,state)

session.start()