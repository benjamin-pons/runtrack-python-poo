import random

class Personnage:
    def __init__(self, nom: str, vie: int):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} dégâts !")
        if adversaire.vie <= 0:
            print(f"Il reste {adversaire.vie} points de vie à {adversaire.nom}.")

    def est_vivant(self):
        if self.vie > 0:
            return self.attaquer

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisirNiveau(self):
        print("Choisissez un niveau de difficulté :")
        print("1 - Facile (100 PV)")
        print("2 - Normal (75 PV)")
        print("3 - Difficile (50 PV)")
        choix = input("Votre choix : ")
        
        if choix == "1":
            self.niveau = 100
        elif choix == "2":
            self.niveau = 75
        elif choix == "3":
            self.niveau = 50
        else:
            print("Choix invalide, niveau par défaut : Normal (75 PV)")
            self.niveau = 75

    def lancerJeu(self):
        self.choisirNiveau()
        self.joueur = Personnage("Joueur", self.niveau)
        self.ennemi = Personnage("Ennemi", self.niveau)
        print("Le combat commence !")
        self.deroulementPartie()

    def deroulementPartie(self):
        while self.joueur.est_vivant() and self.ennemi.est_vivant():
            input("Appuyez sur Entrée pour attaquer...")
            self.joueur.attaquer(self.ennemi)
            if self.ennemi.est_vivant():
                self.ennemi.attaquer(self.joueur)
        self.verifierGagnant()

    def verifierGagnant(self):
        if self.joueur.est_vivant():
            print("Bravo ! Vous avez gagné !")
        else:
            print("Dommage... L'ennemi a gagné !")


jeu = Jeu()
jeu.lancerJeu()
