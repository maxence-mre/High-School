import random
import time
import matplotlib.pyplot as plt 




####################### tri par selection ########################
def tri_selection(tab):
   for i in range(len(tab)):

      # Trouver le min
       min = i

       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp

   return tab

###################### tri liste inversé ###################
tab = [random.randint(1,10000) for i in range (10000)]
tab = sorted(tab)
tab.reverse()
#print(tab)
start = time.time()
tri_selection(tab)
end = time.time()
sort_selection = end - start
#print ("Le tableau trié par selection est:")
#for i in range(len(tab)):
#      print ("%d" %tab[i])

print("Tableau trié en",sort_selection, "secondes" )
#########################tri random #################
tab = [random.randint(1,10000) for i in range (10000)]

#print(tab)
start = time.time()
tri_selection(tab)
end = time.time()
sort_selection2 = end - start
#print ("Le tableau trié par selection est:")
#for i in range(len(tab)):
#      print ("%d" %tab[i])

print("Tableau trié en",sort_selection2, "secondes" )

########################tri liste dejà trié ######################
#print(tab)
start = time.time()
tri_selection(tab)
end = time.time()
sort_selection3 = end - start
#print ("Le tableau trié par selection est:")
#for i in range(len(tab)):
#      print ("%d" %tab[i])

print("Tableau trié en",sort_selection3, "secondes" )
print()
print()

   




   


######################## tri par insertion   #########################

# Programme Python pour l'implémentation du tri par insertion
def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k


#################################### tri liste inversé##############################
tab = [random.randint(1,10000) for i in range (10000)]
tab = sorted(tab)
tab.reverse()
#print(tab)
start = time.time()
tri_insertion(tab) 
#print ("Le tableau trié par insertion est:")
#for i in range(len(tab)): 
#    print ("% d" % tab[i])

end  = time.time()
sort_insertion = end - start 
print("Tableau trié en",sort_insertion, "secondes" )
######################tri random #################################
tab = [random.randint(1,10000) for i in range (10000)]
#print(tab)
start = time.time()
tri_insertion(tab) 
#print ("Le tableau trié par insertion est:")
#for i in range(len(tab)): 
#    print ("% d" % tab[i])

end  = time.time()
sort_insertion2 = end - start 
print("Tableau trié en",sort_insertion2, "secondes" )

#######################tri liste deja trié##################################

#print(tab)
start = time.time()
tri_insertion(tab) 
#print ("Le tableau trié par insertion est:")
#for i in range(len(tab)): 
#    print ("% d" % tab[i])

end  = time.time()
sort_insertion3 = end - start 
print("Tableau trié en",sort_insertion3, "secondes" )
print()
print()




############################## tri a bulles ###############################

# Programme Python pour l'implémentation du Tri à bulle
def tri_bulle(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]


################################## tri liste inversé #############################
tab = [random.randint(1,10000) for i in range (10000)]
tab = sorted(tab)
tab.reverse()
#print(tab)
 
start = time.time()
tri_bulle(tab)
 
#print ("Le tableau trié par bulle est:")
#for i in range(len(tab)): 
#    print ("% d" % tab[i])
end = time.time()
sort_bulle = end - start
print("Tableau trié en",sort_bulle, "secondes" )


#######################tri random ############################

tab = [random.randint(1,10000) for i in range (10000)]
#print(tab)
start = time.time()
tri_bulle(tab)
#print ("Le tableau trié par bulle est:")
#for i in range(len(tab)): 
#    print ("% d" % tab[i])
end = time.time()
sort_bulle2 = end - start
print("Tableau trié en",sort_bulle2, "secondes" )

########################liste deja trié ################################
start = time.time()
tri_bulle(tab)
#print ("Le tableau trié par bulle est:")
#for i in range(len(tab)): 
#    print ("% d" % tab[i])
end = time.time()
sort_bulle3 = end - start
print("Tableau trié en",sort_bulle3, "secondes" )
print()
print()

############# Tri par fusion ######################

#Tri fusion fonction de division du tableau
def tri_fusion(tableau):
    if  len(tableau) <= 1: 
        return tableau
    pivot = len(tableau)//2
    tableau1 = tableau[:pivot]
    tableau2 = tableau[pivot:]
    gauche = tri_fusion(tableau1)
    droite = tri_fusion(tableau2)
    fusionne = fusion(gauche,droite)
    return fusionne


#Tri fusion fonction de fusion de 2 listes
def fusion(tableau1,tableau2):
    indice_tableau1 = 0
    indice_tableau2 = 0    
    taille_tableau1 = len(tableau1)
    taille_tableau2 = len(tableau2)
    tableau_fusionne = []
    while indice_tableau1<taille_tableau1 and indice_tableau2<taille_tableau2:
        if tableau1[indice_tableau1] < tableau2[indice_tableau2]:
            tableau_fusionne.append(tableau1[indice_tableau1])
            indice_tableau1 += 1
        else:
            tableau_fusionne.append(tableau2[indice_tableau2])
            indice_tableau2 += 1
    while indice_tableau1<taille_tableau1:
        tableau_fusionne.append(tableau1[indice_tableau1])
        indice_tableau1+=1
    while indice_tableau2<taille_tableau2:
        tableau_fusionne.append(tableau2[indice_tableau2])
        indice_tableau2+=1
    return tableau_fusionne
#########################tri liste inversé################################
tableau = [random.randint(1,1000000) for i in range (1000000)]
tableau = sorted(tab)
tableau.reverse()
#print(tableau)
start = time.time()
tableau_trie = tri_fusion(tableau)
#print(tableau_trie)
end = time.time()
sort_fusion = end - start
print("Tableau trié en",sort_fusion, "secondes" )
##############################tri random ####################################

tableau = [random.randint(1,1000000) for i in range (1000000)]
#print(tableau)
start = time.time()
tableau_trie = tri_fusion(tableau)
#print(tableau_trie)
end = time.time()
sort_fusion2 = end - start
print("Tableau trié en",sort_fusion2, "secondes" )

############################tri liste deja trié #######################################

start = time.time()
tableau_trie = tri_fusion(tableau)
#print(tableau_trie)
end = time.time()
sort_fusion3 = end - start
print("Tableau trié en",sort_fusion3, "secondes" )

#########################################################################


barwidth = 0.2
etiquettes = ['Selection', 'insertion', 'bulle', 'fusion']
valeurs = [sort_selection, sort_insertion, sort_bulle, sort_fusion]
valeurs2 = [sort_selection2, sort_insertion2, sort_bulle2, sort_fusion2]
valeurs3 = [sort_selection3, sort_insertion3, sort_bulle3, sort_fusion3]
r1 = range(len(valeurs))
r2 = [x + barwidth for x in r1]
r3 = [x + 2* barwidth for x in r1]

plt.bar(r1, valeurs, width = barwidth, color = ['yellow' for i in valeurs],
        edgecolor = ['blue' for i in valeurs])
plt.bar(r2, valeurs2, width = barwidth, color = ['pink' for i in valeurs],
        edgecolor = ['green' for i in valeurs])
plt.bar(r3, valeurs3, width = barwidth, color = ['green' for i in valeurs],
        edgecolor = ['green' for i in valeurs])
plt.xticks([r + barwidth / 2 for r in range(len(valeurs))],
           ['Selection', 'Insertion','Bulle','Fusion'])

plt.xlabel("noms des algos ")
plt.ylabel("Temps d'execution")
plt.title ('Histogramme du temps d execution de 4 algos de tri' )
plt.savefig("Histogramme temps d'execution de 4 algos de tri")

plt.show()
