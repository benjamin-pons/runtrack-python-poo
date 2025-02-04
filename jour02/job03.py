class Livre:
    def __init__(self, titre, nb_pages, auteur):
        self.__titre = titre
        self.__auteur = auteur
        self.set_nb_pages(nb_pages)  
        self.__disponible = True

    # Getters
    def get_titre(self):
        return self.__titre

    def get_nb_pages(self):
        return self.__nb_pages  

    def get_auteur(self):
        return self.__auteur

    # Setters
    def set_titre(self, titre):
        self.__titre = titre

    def set_nb_pages(self, nb_pages):
        if nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            self.__nb_pages = 0 
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible =False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu.")
        else:
            print(f"Le livre '{self.__titre}' était déjà disponible.")

livre = Livre("Coco", 58, "Walt Disney")
print("Livre :", livre.get_titre())
print("Nombre de pages :", livre.get_nb_pages())  
print("Auteur :", livre.get_auteur())

print("Livre disponible ?", livre.verification())


livre.emprunter()


print("Livre disponible ?", livre.verification())


livre.emprunter()


livre.rendre()

print("Livre disponible ?", livre.verification())

livre.rendre()

livre.set_nb_pages(120)

print("Nouveau nombre de pages :", livre.get_nb_pages())