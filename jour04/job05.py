class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix} €")

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes : {self.portes}")

    def demarrer(self):
        print(f"La voiture {self.marque} {self.modele} démarre en douceur. Vroom vroom !")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues : {self.roue}")

    def demarrer(self):
        print(f"La moto {self.marque} {self.modele} rugit en démarrant. Vroom !")



vehicule = Vehicule("Volkswagen", "Golf4", 2000, 1900)
vehicule.informationsVehicule()
vehicule.demarrer()  

print("\n-----\n")


voiture = Voiture("Renault", "Clio", 2020, 18000)
voiture.informationsVehicule()
voiture.demarrer()  

print("\n-----\n")


moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationsVehicule()
moto.demarrer()  
