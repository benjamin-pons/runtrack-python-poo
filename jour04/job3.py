class Rectangle :
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

#getteur
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur


#setteur
    def set_longueur(self,longueur):
        self.__longueur = longueur

    def set_largeur(self,largeur):
        self.__largeur = largeur

    

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede (Rectangle):
    def __init__(self,hauteur,longueur,largeur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
        


    def get_hauteur(self):
        return self.__hauteur


    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur


    def volume(self):
        return self.surface() * self.__hauteur



rectangle = Rectangle(5,3)
print(f"Périmètre du rectangle : {rectangle.perimetre()}")
print(f"Surface du rectangle : {rectangle.surface()}")


rectangle.set_longueur(8)
rectangle.set_largeur(4)
print(f"Nouveau périmètre du rectangle : {rectangle.perimetre()}")
print(f"Nouvelle surface du rectangle : {rectangle.surface()}")

parallelepipede = Parallelepipede(5, 3, 10)
print(f"Volume du parallélépipède : {parallelepipede.volume()}")