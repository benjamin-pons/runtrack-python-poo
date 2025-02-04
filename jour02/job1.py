class Rectangle :
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur = largeur

# Accesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

# Mutateurs (setters)
    def set_longueur(self,longueur):
        self.__longueur = longueur

    def set_largeur(self,largeur):
        self.__largeur = largeur

rect = Rectangle(10, 5)

print("longueur :", rect.get_longueur())
print("largeur: ",rect.get_largeur())

rect.set_longueur(15)
rect.set_largeur(8)

print("Nouvelle longueur : " ,rect.get_longueur())
print("Nouvelle largeur:" ,rect.get_largeur())