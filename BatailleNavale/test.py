A=[0,0,0,0,0,0,0,0,0,0]     #
B=[0,0,0,0,0,0,0,0,0,0]     #
C=[0,0,0,0,0,0,0,0,0,0]     #
D=[0,0,0,0,0,0,0,0,0,0]     #
E=[0,0,0,0,0,0,0,0,0,0]     #   Initialisation de la table de jeu
F=[0,0,0,0,0,0,0,0,0,0]     #
G=[0,0,0,0,0,0,0,0,0,0]     #
H=[0,0,0,0,0,0,0,0,0,0]     #
I=[0,0,0,0,0,0,0,0,0,0]     #
J=[0,0,0,0,0,0,0,0,0,0]     #

tab=[[0,0,0,0,0,0,0,0,0,0],     # methode prof     for i in range(10):
...                             #                        t.append([0]*10)
    [0,0,0,0,0,0,0,0,0,0],     #

CarteJoueur=[A,B,C,D,E,F,G,H,I,J]

dico_x={"A":A,"B":B,"C":C,"D":D,"E":E,"F":F,"G":G,"H":H,"I":I,"J":J}
dico_y={"1":A,"2":B,"3":C,"4":D,"5":E,"6":F,"7":G,"8":H,"9":I,"10":J}
dico_y1={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10}

def PorteAvion():                                                       # peut etre ameliorer grace a des parametres
    sens = input("sens horizontal ou vertical : ")
    originex = input("lettre de la premiere case : ")
    originey = input("numero de cette meme case : ")
    originey = int(originey)

    if sens == "horizontal" :
        while 10-originey < 4 :                                                                             # evite les sorties de map      
            originey = input("sortie de map, entrez un nouveau numero pour cette meme case : ")             #                               
            originey = int(originey)                                                                        #
        x = dico_x[originex]
        for i in range(5):
            x[originey + (i-1)] = "PorteAvion"

    if sens == "vertical":
        testx=originex                                                                                      # evite les sorties de map
        x=dico_y1[testx]                                                                                    # 
        while x+4>10:                                                                                       #
            originex=input("sortie de map, entrez une nouvelle lettre pour la premiere case : ")            #
            testx=originex                                                                                  #
            x=dico_y1[testx]                                                                                #
        for i in range(5) :
            x=dico_y1[originex]                     # transforme la lettre en chiffre pour pouvoir l'incrementer
            x=x+i                                   # increment
            charles=dico_y[str(x)]                  # str permet de change le type en chaine de caractere / retransforme le chiffre en lettre de la table de jeu
            charles[originey] = "PorteAvion"        # pose le porte avion

PorteAvion()

print(CarteJoueur)
