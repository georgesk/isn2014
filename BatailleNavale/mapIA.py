# -*- coding: cp1252 -*-

"""
@file mapIA.py

Ce fichier fait partie du projet Batnav
Batnav est un petit logiciel libre, vous avez le droit de le réutiliser à
votre convenance, dans le respect de la licence GPL V3, ou, selon vos
préférences, de toute version ultérieure de celle-ci.
Le texte de la licence est disponible à http://www.gnu.org/licenses/gpl.html
"""


import random

def map() :
    """
    Initialisation de terrain de jeu vide
    @return un tableau 10 x 10 rempli avec des zéros
    """
    tab=[[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
    return tab


class bateau(object):
    """
    classe pour implémenter les bateaux
    """
    def __init__(self,longueur=0,sens=0,originex=0,originey=0,name="",statut="entier"):
        """
        le constructeur
        @param longueur taille du bateau
        @param sens 0 vertical et 1 horizontal
        @param originex abscisse de la premiere case du bateau
        @param originey ordonnée de la premiere case du bateau
        @param name nom du bateau
        """
        self.longueur = longueur
        self.sens = sens
        self.originex = originex
        self.originey = originey
        self.name = name
        self.pv = longueur
        self.statut = statut
        
    def __str__(self):
        return "bateau {} sens : {} orgx : {} orgy : {}".format(self.name,self.sens,self.originex,self.originey)

utilise = []
utiliseIA = []



PorteAvion = bateau(longueur=5,name="Porte avion")
Croiseur = bateau(longueur=4,name="Croiseur")
ContreTorpilleur = bateau(longueur=3,name="Contre-torpilleur")
SousMarin = bateau(longueur=3,name="Sous marin")
Torpilleur1 = bateau(longueur=2,name="Torpilleur 1")
Torpilleur2 = bateau(longueur=2,name="Torpilleur 2")



CarteJoueur = map()
CarteIA = map()

l=[PorteAvion,Croiseur,ContreTorpilleur,SousMarin,Torpilleur1,Torpilleur2]


def utilisateur():
    """
    permet de définir la carte de jeu du joueur
    """
    global CarteJoueur
    utilise = []
    for i in range(len(l)):
        print(l[i].name)
        l[i].sens = int(input("sens 1 = horizontal ou 0 = vertical "))
        l[i].originex = int(input("numero de la colonne de la premiere case : "))
        l[i].originey = int(input("numero de la ligne de la premiere case : "))
        print(l[i])                     #espion
        if l[i].sens == 1 :
            for k in range(l[i].longueur):
                CarteJoueur[l[i].originey][l[i].originex + k] = l[i].name
                coord=(l[i].originex + k,l[i].originey)
                utilise.append(coord)
        if l[i].sens == 0 :
            for k in range(l[i].longueur):
                CarteJoueur[l[i].originey + k][l[i].originex] = l[i].name
                coord=(l[i].originex,l[i].originey + k)
                utilise.append(coord)
        print(utilise)                  #espion
        print(CarteJoueur)              #espion

def ordi():
    """
    permet de définir une carte aléatoire
    """
    global CarteIA
    utiliseIA = []
    for i in range(len(l)):
        condition = False
        while condition == False:
            test = []
            l[i].sens = random.randint(0,1)
            if l[i].sens == 1:                      #sens horizontal
                l[i].originex = random.randint(0,9 - l[i].longueur)
                l[i].originey = random.randint(0,9)
            else:
                l[i].originex = random.randint(0,9)
                l[i].originey = random.randint(0,9 - l[i].longueur)
            for k in range(l[i].longueur):
                if l[i].sens == 1:
                    coord = (l[i].originex + k,l[i].originey)
                    test.append(coord)
                else:
                    coord = (l[i].originex,l[i].originey + k)
                    test.append(coord)
            if set(utiliseIA) & set(test):
                condition = False
                print("recommence")                 #espion
            else:
                condition = True
                print("continue")                   #espion
        if l[i].sens == 1 :
            for k in range(l[i].longueur):
                CarteIA[l[i].originey][l[i].originex + k] = l[i].name
                coord=(l[i].originex + k,l[i].originey)
                utiliseIA.append(coord)
        if l[i].sens == 0 :
            for k in range(l[i].longueur):
                CarteIA[l[i].originey + k][l[i].originex] = l[i].name
                coord=(l[i].originex,l[i].originey + k)
                utiliseIA.append(coord)
    return CarteIA

lis=["Porte avion","Croiseur","Contre-torpilleur","Sous marin","Torpilleur 1","Torpilleur 2"]
li=["PAD","CRD","CTD","SSD","T1D","T2D"]
def init(dico):
    """
    permet de transformer un dictionnaire python contenant des positions de bateaux en une liste
    @param dico dictionnaire python
    """
    for i in range(len(li)):
        for j in range(len(dico[li[i]])):
            x=dico[li[i]][j]["x"]
            y=dico[li[i]][j]["y"]
            CarteJoueur[y-1][x-1]=lis[i]
    return CarteJoueur
