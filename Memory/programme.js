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
	var liste= new Array(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24);
	var tab = new Array();
	a=0;
	while(liste.length != 0){
		n = Math.floor((Math.random() * liste.length));
		tab[a]=liste[n];
}
}
