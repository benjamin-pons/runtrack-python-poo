class Student :
    nb_credit = 0
    def __init__(self,nom,prenom,numero_etudiant,nb_credit):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__nb_credit = nb_credit
        self.__level = self.__student_eval()

    def get_credit(self):
        return self.nb_credit

    #set
    def add_credits(self,nb_credit):
        if nb_credit < 0:
            print("erreur")
        else :
            self.__nb_credit += nb_credit 
            self.__level = self.__student_eval() 


    def student_info(self): 
        print("nom: ",self.__nom)
        print("Prenom: ",self.__prenom)
        print("id ",self.__numero_etudiant)
        print("Total de credits: ",self.__nb_credit)
        print("Niveau : ", self.__level)

    def __student_eval(self):
        if self.__nb_credit >= 90:
            return "Excellent"
        elif self.__nb_credit >= 80:
            return "Très bien"
        elif self.__nb_credit >= 70:
            return "Bien"
        elif self.__nb_credit>= 60:
            return "Passable"
        else:
            return "Insuffisant"


student = Student("John","Doe",8840,0)

student.student_info()

student.add_credits(15)
student.add_credits(80)
student.add_credits(15)

student.student_info()
