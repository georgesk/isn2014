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

dico_x={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}

def PorteAvion(sens,originex,originey) :
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
        while x+4>9 :                                                                                       # evite les sorties de map
            originex = input("sortie de map, entrez une nouvelle lettre pour cette meme case : ")           #
            x = dico_x[originex]                                                                            #
        
        for i in range(5) :
            CarteJoueur[x+i][originey-1]="PorteAvion"
            

def Croiseur(sens,originex,originey) :
    sens = input("sens horizontal ou vertical : ")                                                                 
    originex = input("lettre de la premiere case : ")                                       
    originey = input("numero de cette meme case : ")                                        
    originey = int(originey)                                                                
    while originey == 0 :
        originey = input("numero de cette meme case : ")                                        
        originey = int(originey)  
                                                                                        
    if sens == "horizontal" :
        while 10-originey < 3 :                                                                             # evite les sorties de map      
            originey = input("sortie de map, entrez un nouveau numero pour cette meme case : ")             #                               
            originey = int(originey) 
    
        x = dico_x[originex]
        for i in range(4):
            CarteJoueur[x][originey+(i-1)]="Croiseur"


    if sens == "vertical" :
        x = dico_x[originex]
        while x+3>9 :                                                                                       # evite les sorties de map
            originex = input("sortie de map, entrez une nouvelle lettre pour cette meme case : ")           #
            x = dico_x[originex]                                                                            #
        
        for i in range(4) :
            CarteJoueur[x+i][originey-1]="Croiseur"
            
            
def ContreTorpilleur(sens,originex,originey) :
    sens = input("sens horizontal ou vertical : ")                                                                 
    originex = input("lettre de la premiere case : ")                                       
    originey = input("numero de cette meme case : ")                                        
    originey = int(originey)                                                                
    while originey == 0 :
        originey = input("numero de cette meme case : ")                                        
        originey = int(originey)  
                                                                                        
    if sens == "horizontal" :
        while 10-originey < 2 :                                                                             # evite les sorties de map      
            originey = input("sortie de map, entrez un nouveau numero pour cette meme case : ")             #                               
            originey = int(originey) 
    
        x = dico_x[originex]
        for i in range(3):
            CarteJoueur[x][originey+(i-1)]="ContreTorpilleur"


    if sens == "vertical" :
        x = dico_x[originex]
        while x+2>9 :                                                                                       # evite les sorties de map
            originex = input("sortie de map, entrez une nouvelle lettre pour cette meme case : ")           #
            x = dico_x[originex]                                                                            #
        
        for i in range(3) :
            CarteJoueur[x+i][originey-1]="ContreTorpilleur"


def SousMarin(sens,originex,originey) :
    sens = input("sens horizontal ou vertical : ")                                                                 
    originex = input("lettre de la premiere case : ")                                       
    originey = input("numero de cette meme case : ")                                        
    originey = int(originey)                                                                
    while originey == 0 :
        originey = input("numero de cette meme case : ")                                        
        originey = int(originey)  
                                                                                        
    if sens == "horizontal" :
        while 10-originey < 2 :                                                                             # evite les sorties de map      
            originey = input("sortie de map, entrez un nouveau numero pour cette meme case : ")             #                               
            originey = int(originey) 
    
        x = dico_x[originex]
        for i in range(3):
            CarteJoueur[x][originey+(i-1)]="SousMarin"


    if sens == "vertical" :
        x = dico_x[originex]
        while x+2>9 :                                                                                       # evite les sorties de map
            originex = input("sortie de map, entrez une nouvelle lettre pour cette meme case : ")           #
            x = dico_x[originex]                                                                            #
        
        for i in range(3) :
            CarteJoueur[x+i][originey-1]="SousMarin"


def Torpilleur(sens,originex,originey) :                                                                             
    if sens == "horizontal" :
        x = dico_x[originex]
        for i in range(2):
            CarteJoueur[x][originey+(i-1)]="Torpilleur"

    if sens == "vertical" :    
        for i in range(2) :
            CarteJoueur[x+i][originey-1]="Torpilleur"


    

def sens():
    sens = input("sens horizontal ou vertical : ")  
    return sens
    
def originex(sens):
    originex = input("lettre de la premiere case : ")
    if sens == "vertical" :
        x = dico_x[originex]
        while x+1>9 :                                                                                       # evite les sorties de map
            originex = input("sortie de map, entrez une nouvelle lettre pour cette meme case : ")           #
            x = dico_x[originex]     
    return originex
            
def originey(sens):
    originex = input("lettre de la premiere case : ")
    if sens == "vertical" :
        x = dico_x[originex]
        while x+1>9 :                                                                                       # evite les sorties de map
            originex = input("sortie de map, entrez une nouvelle lettre pour cette meme case : ")           #
            x = dico_x[originex]
    return originey







CarteJoueur = map()
CarteAdv = map()


PorteAvion(Init())
Croiseur(Init())
ContreTorpilleur(Init())
SousMarin(Init())
Torpilleur(Init())
print(CarteJoueur)
        
            