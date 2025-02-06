class Joueur:
    def __init__(self, nom, numero, position):
        # Attributs du joueur
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts = 0
        self.__passes = 0
        self.__cartons_jaunes = 0
        self.__cartons_rouges = 0

    # Getters
    def get_nom(self):
        return self.__nom

    def get_numero(self):
        return self.__numero

    def get_position(self):
        return self.__position

    def get_buts(self):
        return self.__buts

    def get_passes(self):
        return self.__passes

    def get_cartons_jaunes(self):
        return self.__cartons_jaunes

    def get_cartons_rouges(self):
        return self.__cartons_rouges


    def marquerUnBut(self):
        self.__buts += 1

    def effectuerUnePasseDecisive(self):
        self.__passes += 1

    def recevoirUnCartonJaune(self):
        self.__cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.__cartons_rouges += 1


    def afficherStatistiques(self):
        print(f"{self.__nom} ({self.__numero}) - Position: {self.__position}")
        print(f"Buts: {self.__buts}, Passes Décisives: {self.__passes}")
        print(f"Cartons Jaunes: {self.__cartons_jaunes}, Cartons Rouges: {self.__cartons_rouges}")
        print("---")

class Equipe:
    def __init__(self, nom):
        # Attributs de l'équipe
        self.__nom = nom
        self.__joueurs = []  # Liste de joueurs

    # Méthode pour ajouter un joueur à l'équipe
    def ajouterJoueur(self, joueur):
        self.__joueurs.append(joueur)

    # Méthode pour afficher les statistiques de tous les joueurs
    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.__nom}:")
        for joueur in self.__joueurs:
            joueur.afficherStatistiques()

    
    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.__joueurs:
            if joueur.get_nom() == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()
                else:
                    print("Action inconnue")
                break


joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
joueur2 = Joueur("Cristiano Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Sergio Ramos", 4, "Défenseur")
joueur4 = Joueur("Kylian Mbappé", 11, "Attaquant")


equipe1 = Equipe("FC Barcelona")
equipe2 = Equipe("Juventus")


equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur4)


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()


equipe1.mettreAJourStatistiquesJoueur("Lionel Messi", "but")
equipe2.mettreAJourStatistiquesJoueur("Cristiano Ronaldo", "passe")
equipe2.mettreAJourStatistiquesJoueur("Kylian Mbappé", "carton_jaune")


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
