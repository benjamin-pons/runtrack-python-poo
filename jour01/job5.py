class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Les coordonnées sont : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée X : {self.x}")

    def afficherY(self):
        print(f"Coordonnée Y : {self.y}")

    def changerX(self):
        self.x = int(input("Nouvelle coordonnée X : "))  
        print(f"Les coordonnées sont maintenant : ({self.x}, {self.y})")

    def changerY(self):
        self.y = int(input("Nouvelle coordonnée Y : "))  
        print(f"Les coordonnées sont maintenant : ({self.x}, {self.y})")


point = Point(3, 5)

point.afficherLesPoints()

point.changerX()

point.changerY()
