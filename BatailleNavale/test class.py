

def map() :
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
    def __init__(self,longueur=0,sens=0,originex=0,originey=0,nombre=1,name=""):
        self.longueur = longueur
        self.sens = sens
        self.originex = originex
        self.originey = originey
        self.nombre = nombre
        self.name = name
        
    def __str__(self):
        return "bateau {} sens : {} orgx : {} orgy : {}".format(self.name,self.sens,self.originex,self.originey)

utilise = []



PorteAvion = bateau(longueur=5,name="PorteAvion")
Croiseur = bateau(longueur=4,name="Croiseur")
ContreTorpilleur = bateau(longueur=3,name="ContreTorpilleur")
SousMarin = bateau(longueur=3,name="SousMarin")
Torpilleur = bateau(longueur=2,nombre=2,name="Torpilleur")




CarteJoueur = map()

l=[PorteAvion,Croiseur,ContreTorpilleur,SousMarin,Torpilleur]

for i in range(len(l)):
    for j in range(l[i].nombre):
        print(l[i].name)
        l[i].sens = int(input("sens 1 = horizontal ou 0 = vertical "))
        l[i].originex = int(input("numero de la colonne de la premiere case : "))
        l[i].originey = int(input("numero de la ligne de la premiere case : "))
        print(l[i])
        if l[i].sens == 1 :
            for k in range(l[i].longueur):
                print(l[i].originex + k)
                print("bonjour")
                CarteJoueur[l[i].originey][l[i].originex + k] = l[i].name
                coord=(l[i].originex + k,l[i].originey)
                utilise.append(coord)
        print(utilise)
        print(CarteJoueur)
        
                    
        
        
