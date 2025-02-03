class personne:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
        

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

nom = input ("Entre ton nom: ")
prenom = input("Entre ton prénom : ")


personne = personne(nom, prenom)

print(personne.SePresenter())