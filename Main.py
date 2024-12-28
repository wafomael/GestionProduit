from Gestion_stock.State.Impl.InMemory.Impl.InMemoryStateMenue import InMemoryStateMenue
from Gestion_stock.Repository.impl.InMemoryProduitRepository import InMemoryProduitRepository
from Gestion_stock.Repository.impl.InMemoryVenteRepository import InMemoryVenteRepository
from Utilisateur import Utilisateur
from Session import Session

produit = InMemoryProduitRepository([])
vente = InMemoryVenteRepository([])

utilisateur = Utilisateur("franck")

state = InMemoryStateMenue()

session = Session(utilisateur,vente,produit,state)

session.start()