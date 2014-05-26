
/**
Serviront à déterminer un gagnant 
**/
var vieIA=19;
var vie=19;

/**
Trace un tableau 10*10 qui contient des cases cliquables, chacunes référencées par une id [ligne,colonne]
@param id l'id de la zone où il sera tracé
**/
function traceAireDeJeu(id){
    var div=$("#"+id);
	var g =$("<p> Carte de jeu de votre adversaire : </p>");
    var t =$("<table>", {cellpadding: "0", id: "tableau"});
    div.append(g);
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
			var td=$("<td>");
			tr.append(td);
			td.append($("<img>", {src: "image/case.png",id:""+id,onclick:"clic(this)",onDblclick:"dbclic(this)"}));
		};
    };
    return t;
};

/**
Trace un tableau 10*10, chaques cases référencées par une id (ligne,colonne)
@param id l'id de la zone où il sera tracé
**/
function traceAireDeJeu1(id){
    var div=$("#"+id);
    var t =$("<table>", {cellpadding: "0", id: "tableau"});
    var g =$("<p> Votre carte de jeu: </p>");
	div.append(g);
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
			var id="("+((lig)-1)+","+((col)-1)+")";
			var td=$("<td>");
			tr.append(td);
			td.append($("<img>", {src: "image/case.png", id:""+id}));
		};
    };
    return t;
};

/**
Ecris un texte
@param id l'id où il sera écrit
**/	
function typeTexte(id){
	var div = $("#"+id);
	var t = $("<p> Un double clique sur une case permet d'attaquer cette cible, un clique droit permet de poser une hypothèse </p>");
	div.append(t);
};

/**
Place une image simulant un bateau dans la zone du joueur
**/
function place() {
	$.getJSON("jeu").done(function(reponse){
		var k = JSON.stringify(reponse);
		var l = JSON.parse(k);
		var m = JSON.stringify(l["carteJoueur"]);
		var n = JSON.parse(m)
		for(lig=0;lig<=9;lig++){
			for(col=0;col<=9;col++){
				if(n[lig][col] != 0){
					var id = "("+lig+","+col+")";
					document.getElementById(id).setAttribute('src','image/case5.png');
				};
			};
		};
	});
}

/**
Fonction appeler dès que possible
**/	
$(document).ready(function(){
    traceAireDeJeu("aireDeJeu2");
    traceAireDeJeu1("aireDeJeu");
	typeTexte("texte");
	place();
});

/**
Définis les actions d'un simple clic sur une case
@param a id de la case cliquée
**/
function clic(a){
	var id = $(a).attr('id');
	id = '#'+id;
	if ($(a).attr('src')=='image/case.png'){
		$(a).attr('src', 'image/case3.png');
	}
	else{
		$(a).attr('src', 'image/case.png');
	};
};

/**
Définis les actions d'un double clic sur une case
@param a id de la case cliquée
**/
function dbclic(a){
	var attaque = new Object;
	var id = $(a).attr("id");
	attaque[0]=new Array;
	var xy={
		x: JSON.parse(id)[1],
		y: JSON.parse(id)[0],
	};
	attaque[0].push(xy);
    $.getJSON( "jeu",{attaque: JSON.stringify(attaque)})
	$.getJSON("arthur","banane").done(function(reponse) {
		var hh = JSON.stringify(reponse);
		hh = JSON.parse(hh);
		if (hh["banane"] == "0"){
			$(a).attr('src', 'image/case4.png');
		}
		else {
			$(a).attr('src', 'image/case2.png');
			$("#bateauTouche").css("display","block").fadeOut( "slow").text("touché "+hh["banane"]+" !");
			vieIA -= 1;
			if(vieIA == 0){
				alert("Félicitation, vous avez gagnez !");
			};
		};
	});
	$.getJSON("arthur","atk").done(function(reponse){
		var jj = JSON.stringify(reponse);
		jj = JSON.parse(jj);
		ll = JSON.stringify(jj["atk"]);
		mm = JSON.parse[ll];
		var id2 = JSON.parse(JSON.stringify(jj["atk"]));
		var id3 = "("+id2["y"]+","+id2["x"]+")";
		var id4 = JSON.stringify(id3);
		var id5 = JSON.parse(id4);
		if (jj["bananier"] == "0"){
			document.getElementById(id5).setAttribute('src','image/case4.png');
		}
		else{
			document.getElementById(id5).setAttribute('src','image/case2.png');
			$("#bateauTouche2").css("display","block").fadeOut( "slow").text("touché "+jj["bananier"]+" !");
			vie -= 1;
			if(vie == 0){
				alert("L'ordinateur a gagné !");
			};
		};		
	});	
};