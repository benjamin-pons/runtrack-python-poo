class Personnage :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x = self.x - 1

    def droite(self):
        self.x = self.x + 1

    def haut(self):
        self.y = self.y + 1

    def bas(self):
        self.y = self.y - 1

    def position(self):
        return(self.x, self.y)
        
personnage = Personnage(x=0,y=0)

print(f"position initial :{personnage.position()}")


personnage.gauche()




print(f"position après déplacements : {personnage.position()}")
