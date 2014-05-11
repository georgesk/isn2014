/**
 * Fichier programme.js
 * Auteur : Thiry G
 * Licence : GPLv2+ 
 * (voir https://www.gnu.org/licenses/license-list.html#SoftwareLicenses)
 * ***********************************
 * Programme très simple en Javascript
 * ***********************************
 **/

function getValue(id){
    return document.getElementById(id).value;
}

function putText(id, newText){
    var e = document.getElementById(id);
    e.innerHTML = newText;
}

/**
 * programme principal
 **/
 
var tab = new Array();
function Rand(){
	var liste = new Array(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24); //liste de nombres de départ
	tab = [];           //liste vide des nombres triés
	a=0;
	while(liste.length != 0){  //tant que liste pas vide
		n = Math.floor((Math.random() * liste.length));     //choisis un nombre aleatoire
		tab[a]=liste[n];
		liste.splice(n,1);
		a=a+1;  //compteur +
    putText("zone2", tab); //affichage
}
}

var secund = false;     //variable indiquant si il s'agit de la 1ere ou 2eme carte
var first;              //variable enregistrant le code de la 1ere carte (#id)
var idfirst;            //variable enristrant l'id de la 1ere carte
var find = false;       //booleen indiquant si le coup est gagné ou non
var coup = 0;           //compteur du nombre de coup

function hh(a){
    if (secund==true){      //test si premier ou deuxieme clic
        img(a);     //execute la fonction img() sur a
        secund=false;
        compare(a);     //execute la fonction compare()
        coup=coup+1;    //compteur de coup
        putText("result", coup);
        if (find==false){       //verifie que 2 cartes sont identiques ou non
            setTimeout(         //timer de 500 ms
                function(){
                    $(first).attr('src', 'img.png');
                    $(a).attr('src', 'img.png');
                }, 
                500
            );
        }else{
            find=false;
        }
    }
    else{
        first="#";
        img(a);
        first = first +  $(a).attr('id');       //code de la premiere carte
        idfirst = $(a).attr('id');      //garde l'id de la premiere carte
        secund=true;
    }

}

function img(a){            //fonction d'affichage de la carte retournee
    var id = $(a).attr('id');
    var val = ((tab[id-1])+(tab[id-1]%2))/2;        //calcule valeur pour l'id en fonction de la liste aleatoire
    if (val==1){$(a).attr('src', 'zz1.png');}       //associe à chaque valeur une image
    if (val==2){$(a).attr('src', 'zz2.png');}
    if (val==3){$(a).attr('src', 'zz3.png');}
    if (val==4){$(a).attr('src', 'zz4.png');}
    if (val==5){$(a).attr('src', 'zz5.png');}
    if (val==6){$(a).attr('src', 'zz6.png');}
    if (val==7){$(a).attr('src', 'zz7.png');}
    if (val==8){$(a).attr('src', 'zz8.png');}
    if (val==9){$(a).attr('src', 'zz9.png');}
    if (val==10){$(a).attr('src', 'zz10.png');}
    if (val==11){$(a).attr('src', 'zz11.png');}
    if (val==12){$(a).attr('src', 'zz12.png');}   
}

function compare(a){            //fonction qui compare la 1ere et 2eme 
    var id = $(a).attr('id');   
    if (tab[id-1]%2==0){        //determine si id est pair ou non
        if (tab[id-1]==tab[idfirst-1]+1){       //compare les deux valeurs
            find = true;
    }
    }
    else{
        if (tab[id-1]==tab[idfirst-1]-1){       //comparaison aussi
            find = true;
    }
    }
}