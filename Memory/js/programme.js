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

function Rand(){
	var liste = new Array(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24); //liste de nombres de départ
	var tab = new Array();  //liste vide des nombres triés
	a=0;
	while(liste.length != 0){  //tant que liste pas vide
		n = Math.floor((Math.random() * liste.length));     //choisis un nombre aleatoire
		tab[a]=liste[n];
		liste.splice(n,1);
		a=a+1;  //compteur +
    putText("zone2", tab); //affichage
}
}

var secund = false;
var first;
function hh(a){
    if (secund==true){   //test si premier ou deuxieme clic
        $(a).attr('src', 'hh.png');    //changer image de la case a
        secund=false;
        setTimeout(   //timer de 500 ms
            function(){     //remise à zero des images
                $(first).attr('src', 'img.png');
                $(a).attr('src', 'img.png');
            }, 
            500
        );
    }
    else{
        first="#";
        $(a).attr('src', '1.png');      //debut d'une suite de modifications avec timer = animations 
        setTimeout(
            function(){$(a).attr('src', '2.png')},200
            );
        setTimeout(
            function(){$(a).attr('src', '3.png')},200
            );
        setTimeout(
            function(){$(a).attr('src', 'hh.png')},200
            );
        first = first +  $(a).attr('id');   //enregistrement id de la premiere case cliquee
        secund=true;
    }

}