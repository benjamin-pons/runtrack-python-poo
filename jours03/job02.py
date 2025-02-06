class CompteBancaire:
    def __init__(self, nom, prenom, solde, decouvert=False):
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert  # Par défaut, le découvert est désactivé

    # Getters
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_solde(self):
        return self.__solde

    # Affichage des informations du compte
    def afficher(self):
        print(f"Nom: {self.__nom}, Prénom: {self.__prenom}, Solde: {self.__solde}€")

    # Affichage du solde
    def solde(self):
        print(f"Votre solde: {self.__solde}€")

    # Versement d'argent sur le compte
    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant}€ effectué. Nouveau solde: {self.__solde}€")
        else:
            print("Le montant du versement doit être positif.")

    # Retrait d'argent du compte
    def retirer(self, montant):
        if montant > 0:
            if self.__solde - montant >= 0 or self.__decouvert:  # Vérifie si le solde permet le retrait ou si le découvert est autorisé
                self.__solde -= montant
                print(f"Retrait de {montant}€ effectué. Nouveau solde: {self.__solde}€")
            else:
                print("Solde insuffisant pour effectuer ce retrait.")
        else:
            print("Le montant du retrait doit être positif.")

    # Appliquer des agios si le solde est négatif
    def agios(self):
        if self.__solde < 0:
            frais = self.__solde * 0.05  # 5% d'agios
            self.__solde -= frais
            print(f"Agios de {frais}€ appliqués. Nouveau solde: {self.__solde}€")
        else:
            print("Aucun agios appliqué. Le solde est positif.")

    # Virement d'un montant à un autre compte
    def virement(self, compte_dest, montant):
        if montant > 0 and self.__solde >= montant:
            self.__solde -= montant
            compte_dest.versement(montant)
            print(f"Virement de {montant}€ effectué vers le compte de {compte_dest.get_nom()}. Nouveau solde: {self.__solde}€")
        else:
            print("Virement impossible. Montant invalide ou solde insuffisant.")


compte1 = CompteBancaire("Pons", "Benjamin", 200, False)
compte2 = CompteBancaire("Lemoine", "Jacques", -100, True)  


compte1.afficher()
compte2.afficher()


compte1.virement(compte2, 100) 


compte1.afficher()
compte2.afficher()
 