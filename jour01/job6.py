class Animal:

    def __init__(self,age,prenom):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age = self.age + 1

    def nommer(self):
        self.prenom= input("nommer l'animal : ")
        print(f"L'animal se nomme {self.prenom}")


mon_animal = Animal(age=0, prenom="prenom")

print(f"L'âge de l'animal est : {mon_animal.age} ans")

mon_animal.vieillir()

print(f"L'âge de l'animal après un an est : {mon_animal.age} ans")

mon_animal.nommer()