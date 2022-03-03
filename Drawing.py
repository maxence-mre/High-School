from PIL.Image import *

i = open("image.png")


def remplissage(r,v,b):
    (largeur, hauteur)= (51,53) #debut de la figure pour remplir l interieur 
    for x in range(largeur): #debut de la boucle pour recursivite 
         for y in range(hauteur):
            (r,v,b) = (255,0,0) #remplissage en rouge 
            i.putpixel((x,y),(r,v,b))

Image.show(i)
