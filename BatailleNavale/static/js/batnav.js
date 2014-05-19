/**
 * Programmes et fonctions utilisés pour la bataille navale
 * les bibliothèques jQuery et jQuery-ui sont utilisées
 **/

/**
 * définitions des bateaux disponibles
 **/
var laFlotte = {
    PA: {img: "PorteAvion",       l:5},
    CR: {img: "Croiseur",         l:4},
    SS: {img: "SousMarin",        l:3},
    CT: {img: "ContreTorpilleur", l:3},
    T1: {img: "Torpilleur",       l:2},
    T2: {img: "Torpilleur",       l:2},
};

var coord = new Array();
/**
 * identification d'une image draggable
 * @param jQobj un objet de type jQuery
 * @return un objet {img: <nom caractéristique>, sens: 'v' ou 'h'}
 **/
function identifieDraggable(jQobj){
    var s = jQobj.attr("src");
    var m = s.match(/image\/(.*)DraggableV\.jpg/);
    if (m) return {img: m[1], sens: "h"};
    m=s.match(/image\/(.*)Draggable\.jpg/);
    return {img: m[1], sens: "v"};
}

/**
 * détermine l'image draggable associée à un bateau
 * @param nom le nom du bateau "PorteAvion", etc.
 * @param sens "h" ou "v"
 * @return chemin vers la bonne image
 **/
function bateauSrc(nom, sens){
    if (sens == "v") return "image/"+nom+"DraggableV.jpg";
    else return "image/"+nom+"Draggable.jpg";
}

/**
 * trace l'aire de jeu sous forme d'un tableau de 10x10 cases dans
 * un bloc désigné par son id.
 * @param id l'identifiant du bloc où on place l'aire de jeu
 * @return l'objet jQuery contenant le tableau créé
 **/
function traceAireDeJeu(id){
    var div=$("#"+id);
    var t  =$("<table>", {cellpadding: "0", id: "tableau"});
    div.append(t);
    var tr=$("<tr>");
    /* première ligne d'en-tête */
    t.append(tr);
    tr.html("<th></th>");
    for(var col=1; col<=10; col++){tr.append($("<th>").html(col))}
    for(var lig=1; lig <=10; lig++){
	tr=$("<tr>");
	t.append(tr);
	tr.append($("<td>").html(" ABCDEFGHIJ".charAt(lig)));
	for(col=1; col <=10; col++){
	    var id="["+lig+","+col+"]";
	    var td=$("<td>",{id: id, content: "0"});
	    tr.append(td);
	    var fnMaker = function(id) {
		return function(ev, ui){
		    //alert("dropped into "+id+$(ui.draggable).find("img").attr("src"));
		    var i= identifieDraggable(ui.draggable);
			coord.push(""+i["img"]+" "+id+" "+i["sens"]);
			alert(coord);
		}
	    };
	    $(td).droppable({
		drop: fnMaker(id)
	    });
	    td.append($("<img>", {src: "image/case.png"}));
	}
    }
    return t;
}

/**
 * mise en place des bateaux dans un élément
 * @param id l'identifiant de l'élément où placer les bateaux
 **/
function placeFlotte(id){
    var div=$("#"+id);
    for(var b in laFlotte){
	var nom = laFlotte[b].img;
	var img = $("<img>",{src: "image/"+nom+".jpg", id: b});
	div.append(img);
	img = $("<img>",{src: bateauSrc(nom, "h"), id: b+"D"});
	div.append(img);
	/* la deuxième image de chaque bateau est draggable et on peut la */
	/* faire tourner par un double clic                               */
	img.draggable().rotate({
	    bind: {
		dblclick: function() {
		    var i = identifieDraggable($(this));
		    // basculement du sens de l'image
		    var sens = "h";
		    if (i["sens"] == "h") sens = "v";
		    $(this).attr("src", bateauSrc(i["img"],sens));
		}
	    }
	});
	
    }
}

$(document).ready(function(){
    var t = traceAireDeJeu("aireDeJeu");
    placeFlotte("bateaux");
});

