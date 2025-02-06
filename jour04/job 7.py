import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"


class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        """Crée un paquet de cartes."""
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))
        
        random.shuffle(self.paquet)  # Mélange le paquet

    def distribuer(self):
        """Distribue 2 cartes à chaque joueur."""
        joueur_main = [self.paquet.pop(), self.paquet.pop()]
        croupier_main = [self.paquet.pop(), self.paquet.pop()]
        return joueur_main, croupier_main

    def valeur_main(self, main):
        """Calcule la valeur totale d'une main."""
        total = 0
        as_count = 0
        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                total += 11
                as_count += 1
            else:
                total += int(carte.valeur)
        
        # Ajuste la valeur des As si nécessaire (passer de 11 à 1 pour éviter de dépasser 21)
        while total > 21 and as_count:
            total -= 10
            as_count -= 1
        
        return total

    def afficher_main(self, main):
        """Affiche les cartes d'une main."""
        return ', '.join([str(carte) for carte in main])

    def tour_croupier(self, croupier_main):
        """Le croupier tire des cartes jusqu'à atteindre au moins 17 points."""
        while self.valeur_main(croupier_main) < 17:
            croupier_main.append(self.paquet.pop())
        return croupier_main

    def jouer(self):
        """Lance une partie de Blackjack."""
        joueur_main, croupier_main = self.distribuer()

        print("Vous avez les cartes suivantes :")
        print(self.afficher_main(joueur_main))
        print("Votre total : ", self.valeur_main(joueur_main))

        # Tour du joueur
        while self.valeur_main(joueur_main) < 21:
            choix = input("Souhaitez-vous prendre une carte (taper 'prendre') ou passer (taper 'passer') ? ").strip().lower()
            if choix == 'prendre':
                joueur_main.append(self.paquet.pop())
                print("Vous avez maintenant les cartes suivantes :")
                print(self.afficher_main(joueur_main))
                print("Votre total : ", self.valeur_main(joueur_main))
            elif choix == 'passer':
                break

        if self.valeur_main(joueur_main) > 21:
            print("Désolé, vous avez dépassé 21 points. Vous avez perdu.")
            return

        
        croupier_main = self.tour_croupier(croupier_main)
        print("\nLe croupier a les cartes suivantes :")
        print(self.afficher_main(croupier_main))
        print("Total du croupier : ", self.valeur_main(croupier_main))

        # Détermine le gagnant
        if self.valeur_main(croupier_main) > 21:
            print("Le croupier a dépassé 21 points. Vous avez gagné !")
        elif self.valeur_main(joueur_main) > self.valeur_main(croupier_main):
            print("Félicitations, vous avez gagné !")
        elif self.valeur_main(joueur_main) < self.valeur_main(croupier_main):
            print("Le croupier a gagné.")
        else:
            print("C'est une égalité.")


jeu = Jeu()
jeu.jouer()
