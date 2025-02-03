class operation:
    nombre1 = 2
    nombre2 = 3
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        

    def addition(self):
        return self.nombre1 +self.nombre2




operation = operation(nombre1=2,nombre2=3)
print(operation.addition())
