class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut

    # Getters
    def get_titre(self):
        return self.__titre

    def get_description(self):
        return self.__description

    def get_statut(self):
        return self.__statut

    # Setter pour le statut
    def set_statut(self, statut):
        if statut in ["à faire", "terminée"]:
            self.__statut = statut
        else:
            print("Statut invalide, il doit être 'à faire' ou 'terminée'.")

    
    def afficher(self):
        print(f"Titre: {self.__titre}, Description: {self.__description}, Statut: {self.__statut}")

class ListeDeTaches:
    def __init__(self):
        self.__taches = []


    def ajouterTache(self, tache):
        self.__taches.append(tache)

  
    def supprimerTache(self, titre):
        for tache in self.__taches:
            if tache.get_titre() == titre:
                self.__taches.remove(tache)
                print(f"Tâche '{titre}' supprimée.")
                return
        print(f"Aucune tâche trouvée avec le titre '{titre}'.")


    def marquerCommeFinie(self, titre):
        for tache in self.__taches:
            if tache.get_titre() == titre:
                tache.set_statut("terminée")
                print(f"Tâche '{titre}' marquée comme terminée.")
                return
        print(f"Aucune tâche trouvée avec le titre '{titre}'.")


    def afficherListe(self):
        if not self.__taches:
            print("Aucune tâche dans la liste.")
        else:
            for tache in self.__taches:
                tache.afficher()


    def filterListe(self, statut):
        filtered_taches = [tache for tache in self.__taches if tache.get_statut() == statut]
        if filtered_taches:
            for tache in filtered_taches:
                tache.afficher()
        else:
            print(f"Aucune tâche trouvée avec le statut '{statut}'.")
