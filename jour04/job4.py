import math

class Forme :
    def aire():
        return 0

class Cercle(Forme):
    def __init__(self,radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius ** 2
    
class Rectangle(Forme):
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

cercle = Cercle(4)
print(f"Voici l'aire du cercle: {cercle.aire()}")
rectangle = Rectangle(4,8)
print(f"voici l'aire du rectangle : {rectangle.aire()}")


