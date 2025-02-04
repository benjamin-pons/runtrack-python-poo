class Livre:
    def __init__(self, titre, nb_pages, auteur):
        self.__titre = titre
        self.__auteur = auteur
        self.set_nb_pages(nb_pages)  

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

livre = Livre("Coco", 58, "Walt Disney")
print("Livre :", livre.get_titre())
print("Nombre de pages :", livre.get_nb_pages())  
print("Auteur :", livre.get_auteur())

livre.set_nb_pages(120)
print("Nouveau nombre de pages :", livre.get_nb_pages())




