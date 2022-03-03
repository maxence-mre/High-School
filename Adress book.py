carnet ={}
def ajout() : #choix 1
    nom=input("nouveau contact : ")
    if nom in carnet :
        print("Le nom existe dejà")
    else :
        num=input("adresse : ")
        print("contact enregistré")
        carnet[nom]=num 
        d = nom

        
        
    

            
def delete() : #choix 2
    d = input("Entrez le nom à supprimer : ")
    if d in carnet :
        del carnet[d]
        print("Contact supprimé")
        return
    else :
        print("Contact inexistant")
        reessai = input("Reessayer ? oui : tapez 0 / non : tapez 1")
        while reessai != 1 :
            if reessai == 0 :
                delete()
            else :
                print("Entrez une valeur valide ")
                break


          
    
def modifier(): #choix 3
    modif = input("Entrez le contact à modifier : ")
    if modif in carnet :
        nouveau_nom = input("Entrez le nouveau nom : ")
        nouveau_num = input("Entrez la nouvelle adresse : ")
        carnet[nouveau_nom]=nouveau_num
        print("Contact modifié")
        return
    else : 
        print ("Contact inexistant")
        reessai=input("Reessayer ? oui : tapez 0 / non : tapez 1")
        while reessai != 1 :
            if reessai == 0 :
                modifier ()
            else :
                print("Entrez une valeur valide ")
                break 

                
   
    
def search(): #choix 4,
#pour chercher le numéro avec le nom
    for liste in carnet:
        nom, num = liste
        if nom == num:
            return num

    
def fusion(): #choix 5
    pass
    
def afficher(): #choix 6
#pour afficher la liste de tous les noms et numéros.
    for liste in carnet:
        nom, num = liste
        print("{0} -----> {1}".format(nom, num))
        return
    
    #programme principal 
    
print("1 : entrer un nouveau contact \n2 : supprimer une adresse")
print("3 : modifier \n4 : rechercher par le nom")
print("5 : fusionner deux adresses \n6 : afficher le carnet")
print("Tapez 0 pour sortir ")
choix=input("votre choix : ")
while choix != "0" : 
    
    if choix =="1":
        ajout()
    elif choix=="2":
        delete ()
    elif choix== "3":
        modifier()
    elif choix=="4":
        recherche =input("Quel est le nom du contact")
        print(search(recherche))           
    elif choix =="5":
        fusion()            
    elif choix == "6":
        afficher()            
    else :
        print ("choix invalide")
        choix=input("votre choix : ")
    
  
