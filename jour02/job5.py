class voiture:
    def __init__(self,marque,modele,annee,kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

#getters
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_reservoir(self):
        return self.__reservoir

#setteur
    def set_marque(self,marque):
        self.__marque = marque

    def set_modele(self,modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage

    def set_reservoir(self, litres):
        if 0 <= litres <= 50:
            self.__reservoir = litres
            print("essence mis a jour:", self.__reservoir )
        else:
            print("Erreur : Le réservoir doit être entre 0 et 50 litres.")

    def demarrer(self):
        self.__en_marche = True
        if self.__reservoir > 5:
            print("voiture demarrer")
        else:
            print("⛽ Réservoir trop bas, la voiture ne peut pas démarrer.")

    def arreter(self):
        self.__en_marche = False
        print("voiture arreter")

    def __verifier_plein(self):
        return self.__reservoir

    def afficher_info(self):
            print(f"Marque: {self.__marque}")
            print(f"Modèle: {self.__modele}")
            print(f"Année: {self.__annee}")
            print(f"Kilométrage: {self.__kilometrage} km")
            print(f"En marche: {'Oui' if self.__en_marche else 'Non'}")
            print(f"Réservoir: {self.__reservoir} L")

voiture1 = voiture("Toyota", "Corolla", 2020, 30000)

voiture1.afficher_info()

voiture1.demarrer()

voiture1.afficher_info()

voiture1.set_reservoir(4)
voiture1.demarrer()