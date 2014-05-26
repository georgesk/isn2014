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

/**
 * coord sera une liste de coordonnées liées à une image de bateau.
 * chaque élément de la liste sera un objet de structure
 * { x: <abscisse>, y: <ordonnée>, bateau: <element jquery du bateau>}
 **/
var coord = new Array();

/**
 * identification d'une image draggable
 * @param jQobj un objet de type jQuery
 * @return un objet {img: <nom caractéristique>, sens: 'v' ou 'h'}
 **/
function identifieDraggable(jQobj){
    var img=null, sens=null, l=0;
    var s = jQobj.attr("src");

    var m = s.match(/image\/(.*)DraggableV\.jpg/);
    if (m) { img = m[1]; sens = "v"; }

    m=s.match(/image\/(.*)Draggable\.jpg/);
    if (m) { img = m[1]; sens = "h"; }

    for (bateau in laFlotte){
	if (laFlotte[bateau].img == img){
	    l= laFlotte[bateau].l;
	    break;
	}
    }
    var result = {img: img, sens: sens, longueur: l};
    return result;
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
	    var fnMaker = function(el,lig,col) {
		// cette fonction fabrique une fonction
		// paramètres :
		// el est l'élément qui reçoit le drop
		// li, col sont les coordonnées de cet élément
		return function(ev, ui){
		    // c'est cette fonction-là qui est fabriquée.
		    // paramètres:
		    // ev évènement drop
		    // ui l'élément jquery-ui qui est lâché
		    var i= identifieDraggable(ui.draggable);
		    // on force l'alignement des coins haut-gauche de l'image
		    // lâchée avec la case cible, juste après le drop
		    ui.draggable.position({
			my: "left top",
			at: "left top",
			of: el,
		    });
		    // après l'alignement, on sait quelles cases sont occupées
		    // par le bateau
		    // on efface les anciennes coordonnées du bateau
		    for (var c=0; c < coord.length; c++){
			// ne pas s'occuper des valeurs undefined
			if (! (coord[c])) continue; 
			if ((coord[c].bateau)[0] == (ui.draggable)[0]){
			    // on a bien le même élément DOM
			    // alors on l'efface
			    delete coord[c];
			    // l'élément reste mais il devient indéfini
			}
		    }
		    if (i["sens"]=="h"){
			// si le bateau est horizontal,
			for(var compte=0; compte<i["longueur"]; compte++){
			    var coord_element={
				x: parseInt(col)+compte,
				y: parseInt(lig),
				bateau: ui.draggable,
			    };
			    coord.push(coord_element);
			}
		    } else{
			// si le bateau est vertical,
			for(var compte=0; compte<i["longueur"]; compte++){
			    var coord_element={
				x: parseInt(col),
				y: parseInt(lig)+compte,
				bateau: ui.draggable,
			    };
			    coord.push(coord_element);
			}
		    }
		    // déclenche une information générale
		    informeDesBateaux();
		}
	    };
	    // la bonne fonction drop est fabriquée sur mesure avec les
	    // bons paramètres
	    $(td).droppable({
		drop: fnMaker($(td), lig, col)
	    });
	    td.append($("<img>", {src: "image/case.png"}));
	}
    }
    return t;
}

/**
 * Cette fonction exploite l'information du tableau coord, elles est 
 * appelée quand un bateau est posé.
 **/
function informeDesBateaux(){
    $("#bateauPlace").css("display","block").fadeOut( "slow"); // signal visuel
    // construction de la liste des bateaux posés
    var bateaux= new Object;
    for(var i=0; i < coord.length; i++){
		if(coord[i]){ // pas besoin de retenir les éléments undefined
			var b=coord[i].bateau.attr("id");
			if (! (b in bateaux)){
				// bateau inconnu, on démarre le tableau de ses coordonnées
				bateaux[b] = new Array;
			};
			var xy={
			x: coord[i].x,
			y: coord[i].y,
			};
			bateaux[b].push(xy);
		};
    };
    console.log(JSON.stringify(bateaux));
    $.getJSON( "jeu",{bateaux: JSON.stringify(bateaux)}).done(function(reponse) {
	console.log( reponse );
	$("#debugZone").text(JSON.stringify(reponse));
    });
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
	img = $("<img>",{
	    src: bateauSrc(nom, "h"), 
	    id: b+"D",
	    title: nom+" ; double-clic pour basculer h/v"
	});
	div.append(img);
	/* la deuxième image de chaque bateau est draggable et on peut la */
	/* faire tourner par un double clic                               */
	img.draggable().bind({
	    dblclick: function() {
		console.log("grr ça tourne")
		var i = identifieDraggable($(this));
		// basculement du sens de l'image
		var sens = "h";
		if (i["sens"] == "h") sens = "v";
		$(this).attr("src", bateauSrc(i["img"],sens));
	    },
	});
    };
};

$(document).ready(function(){
	var t = traceAireDeJeu("aireDeJeu");
    placeFlotte("bateaux");
});

