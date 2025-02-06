class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"AGE : {self.age}")

    def Bonjour(self):
        print("bonjour")

    def modifierAge(self,nouvel_age):
        self.age = nouvel_age




class Eleve(Personne) :

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ANS")



class Professeur (Personne) :
    def __init__(self,nom ,matiereEnseignee,age=14):
        super().__init__(age)
        self.nom = nom
        self.__matiereEnseignee = matiereEnseignee
        

    def get_matiereEnseignee(self):
        return self.__matiereEnseignee

    def set_matiereEnseignee(self,matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print(f"le cours de {self.__matiereEnseignee} commencer")


personne = Personne()
personne.afficherAge()

eleve = Eleve()
eleve.afficherAge()

personne.Bonjour()



personne.modifierAge(15)
personne.afficherAge()


eleve = Eleve()
eleve.allerEnCours()


professeur = Professeur(nom="M. Dupont",matiereEnseignee="math", age=40)
professeur.afficherAge() 
professeur.Bonjour()  
professeur.set_matiereEnseignee("math")
professeur.enseigner()  
    