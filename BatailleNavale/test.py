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
CarteJoueur=map()

dico_x={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}

def PorteAvion() :
    sens = input("sens horizontal ou vertical : ")
    originex = input("lettre de la premiere case : ")
    originey = input("numero de cette meme case : ")
    originey = int(originey)
    while originey == 0 :
        originey = input("numero de cette meme case : ")
        originey = int(originey)

    if sens == "horizontal" :
        while 10-originey < 4 :                                                                             # evite les sorties de map      
            originey = input("sortie de map, entrez un nouveau numero pour cette meme case : ")             #                               
            originey = int(originey)

        x = dico_x[originex]
        for i in range(5):
            CarteJoueur[x][originey+(i-1)]="PorteAvion"


    if sens == "vertical" :
        x = dico_x[originex]
        while x+4>9 :
            originex = input("sortie de map, entrez une nouvelle lettre pour cette meme case : ")
            x = dico_x[originex]

        for i in range(5) :
            CarteJoueur[x+i][originey-1]="PorteAvion"

PorteAvion()
print(CarteJoueur)
