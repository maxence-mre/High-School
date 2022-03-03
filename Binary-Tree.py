##########################################################
class ArbreBinaire:
    '''
    Classe permettant de construire un arbre binaire .
    Attributs : valeur ,enfant_gauche , enfant_droit
    '''
    #Constructeur ( un arbre possède à minima un noeud)
    def __init__(self,valeur):
        self.valeur = valeur
        self.enfant_gauche= None
        self.enfant_droit = None
        
    # Méthodes
    def insert_gauche(self,valeur):
        if self.enfant_gauche == None :
            self.enfant_gauche =ArbreBinaire(valeur)
        else:
            new_node=ArbreBinaire(valeur)
            new_node.enfant_gauche=self.enfant_gauche
            self.enfant_gauche=new_node 
            
    def insert_droit(self,valeur):
        if self.enfant_droit == None :
            self.enfant_droit =ArbreBinaire(valeur)
        else:
            new_node=ArbreBinaire(valeur)
            new_node.enfant_droit=self.enfant_droit
            self.enfant_droit=new_node 
            
    def get_valeur(self):
        return self.valeur
    
    def get_gauche(self):
        return self.enfant_gauche
    
    def get_droit(self):
        return self.enfant_droit

class File:

    def __init__(self):
        self.valeurs=[]

    def enfiler(self,valeur):
        self.valeurs.append(valeur)

    def defiler(self):
        return self.valeurs.pop(0)

    def estVide(self):
        return self.valeurs==[]

    def __str__(self):
        return str(self.valeurs)

###########################################################
def Hauteur(T):
    if T!=None :
        x=T
        return 1+max(Hauteur(x.get_gauche()),Hauteur(x.get_droit()))
    else:
        return 0

def Taille(T):
    if T!= None :
        return 1+Taille(T.get_gauche()) + Taille(T.get_droit())
    else:
        return 0

def Infixe(T):
    if T!=None :
        x=T
        Infixe(T.get_gauche())
        print(x.get_valeur())
        Infixe(T.get_droit())
    else :
        return 0
def prefixe(T):
    if T!= None:
        x=T
        print(x.get_valeur())
        prefixe(x.get_gauche())
        prefixe(x.get_droit())

def suffixe(T):
    if T!=None:
        x=T
        suffixe(x.get_gauche())
        suffixe(x.get_droit())
        print(x.get_valeur())

def parcours_largeur(T):
    f=File()
    f.enfiler(T)
    while(f.estVide()==False):
        x=f.defiler()
        print(x.get_valeur())

        if x.get_gauche()!= None :
            TG=x.get_gauche()
            f.enfiler(TG)
        if x.get_droit()!=None :
            
            TD = x.get_droit()
            f.enfiler(TD)
        


def affiche(T):
    if T !=None:
        return (T.get_valeur(),affiche(T.get_gauche()),affiche(T.get_droit()))        



T=ArbreBinaire("A")
T.insert_gauche("B")
T.insert_droit("F")

TB=T.get_gauche()    
TB.insert_gauche("C")
TB.insert_droit("D")

TC=TB.get_gauche()
TC.insert_droit("E")

TF=T.get_droit()
TF.insert_gauche("G")
TF.insert_droit("H")

TG=TF.get_gauche()
TG.insert_gauche("I")

TI=TG.get_gauche()

TH=TF.get_droit()
TH.insert_gauche("J")

TJ=TH.get_droit()




parcours_largeur(T)
print("\n\n\n")
suffixe(T)
print("\n\n\n")
prefixe(T)
print("\n\n\n")

Infixe(T)
print(affiche(T),"\n\n\tLa Hauteur de l arbre est égale à : ",
      Hauteur(T), "\n\n\t La taille de l'arbre est égale à :", Taille(T))
      

