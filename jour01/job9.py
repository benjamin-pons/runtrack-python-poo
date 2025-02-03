class Produit:
    def __init__(self, nom, prixHT, TVA):
        """Initialise un produit avec un nom, un prix HT et une TVA."""
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        """Retourne le prix TTC du produit (prix HT + TVA)."""
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        """Retourne toutes les informations du produit sous forme de chaîne."""
        return f"Nom: {self.nom}\nPrix HT: {self.prixHT}€\nTVA: {self.TVA}%\nPrix TTC: {self.calculerPrixTTC()}€"

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def getPrixTTC(self):
        return self.calculerPrixTTC()


produit1 = Produit("Ordinateur portable", 1000, 20)
produit2 = Produit("Casque audio", 150, 10)
produit3 = Produit("Télévision", 500, 5)


print("Informations avant modification :")
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())


produit1.modifierNom("Ordinateur portable gaming")
produit1.modifierPrix(1200)

produit2.modifierNom("Casque Bluetooth")
produit2.modifierPrix(180)

produit3.modifierNom("Télévision 4K")
produit3.modifierPrix(550)


print("\nInformations après modification :")
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())
