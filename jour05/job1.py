class Part():
    def __init__(self,name,material):
        self.name = name
        self.material = material

    def change_material(self,new_material):
        self.material = new_material

    def __str__(self):
        print(f"nom : {self.name}")
        print(f"materiel: {self.material}")
        
part = Part("bateau","bois")
part.__str__()
part.change_material("metal")
part.__str__()

class ship():
    def __init__(self,nom):
        self.nom = nom
        s

