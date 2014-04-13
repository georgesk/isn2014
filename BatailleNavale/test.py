x=0
y=0

CarteJoueur=[[0]*10]*10
CarteAdversaire=[[0]*10]*10

dico = {"A":CarteJoueur[0],"B":CarteJoueur[1],"C":CarteJoueur[2],"D":CarteJoueur[3],"E":CarteJoueur[4],"F":CarteJoueur[5],"G":CarteJoueur[6],"H":CarteJoueur[7],"I":CarteJoueur[8],"J":CarteJoueur[9]}


CarteAdversaire[1][1]=1

x = input ("x")
y = input (y)

x = dico[x]
print x

if x[y] != 0:
    print ("touche")
else :
    print ("rate")
