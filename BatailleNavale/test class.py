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
    def __init__(self):
        self.longueur = 0
        self.sens = 0
        self.originex = 0
        self.originey = 0
        self.nombre = 0

    def cases(self):
        self.utilise = set([])



PorteAvion = bateau()
Croiseur = bateau()
ContreTorpilleur = bateau()
SousMarin = bateau()
Torpilleur = bateau()

PorteAvion.longueur = 5
PorteAvion.nombre = 1

Croiseur.longueur = 4
Croiseur.nombre = 1

ContreTorpilleur.longueur = 3
ContreTorpilleur.nombre = 1

SousMarin.longueur = 3
SousMarin.nombre = 1

Torpilleur.longueur = 2
Torpilleur.nombre = 2

l=[PorteAvion,Croiseur,ContreTorpilleur,SousMarin,Torpilleur]

for i in range(len(l)):
    for j in range(l[i].nombre):
        l[i].sens = input("sens 1=horizontal ou 2=vertical")
        l[i].originex = input("numero de la colonne de la premiere case du %d",l[i])
        l[i].originey = input("numero de la ligne de la premiere case du %d",l[i])
