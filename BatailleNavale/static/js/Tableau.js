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
	    var id="["+lig+";"+col+"]";
	    var td=$("<td>");
	    tr.append(td);
	    td.append($("<img>", {src: "image/case.png"}));
	}
    }
    return t;
}

$(document).ready(function(){
    var t = traceAireDeJeu("aireDeJeu");
});