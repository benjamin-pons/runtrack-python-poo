class operation:
    nombre1 = 2
    nombre2 = 3
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def afficher_info(self):
        print(f"{self.nombre1} {self.nombre2}")
operation = operation(nombre1=2,nombre2=3)


message1 = "le nombre1 est "
message2 = "le nombre2 est "

print(message1 + str(operation.nombre1))
print(message2 + str(operation.nombre2))

