class Ville : 
    def __init__(self,nom,nombre_habitant):
        self.__nom = nom
        self.__nombre_habitant = nombre_habitant

#getters
    def get_nom(self):
        return self.__nom

    def get_nombre_habitant(self):
        return self.__nombre_habitant

#setteur
    def set_nom(self,nom):
        self.__nom = nom

    def set_nombre_habitant(self, nombre_habitant):
        if nombre_habitant >= 0:
            self.__nombre_habitant = nombre_habitant
        else :
            print("Le nombre d'habitants ne peut pas être négatif.")

    def afficher_infos(self):
        print(f"Ville: {self.__nom}, Habitants: {self.__nombre_habitant}")

class Personne : 
    def __init__(self,nom,age,Ville):
        self.__nom = nom
        self.__age = age
        self.__ville = Ville
        self.ajouterPopulation()


    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville

    def ajouterPopulation(self):
        self.__ville.set_nombre_habitant(self.__ville.get_nombre_habitant() + 1)


Paris = Ville("Paris",1000000)
Marseille = Ville("Marseille",861635)

print("Nombre d'habitants avant l'arrivée des nouvelles personnes :")
Paris.afficher_infos()       
Marseille.afficher_infos()

personne1 = Personne("John", "45", Paris)
personne2 = Personne("Myrtille", "4", Paris)
personne3 = Personne("Chloé"," 18", Marseille)


print("Nombre d'habitants après l'arrivée des nouvelles personnes :")
Paris.afficher_infos()       
Marseille.afficher_infos()   