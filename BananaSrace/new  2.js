<!--
var bulleStyle=null;
if (!document.layers && !document.all && !document.getElementById)
event="chut";  //pour apaiser NN3 et autres antiquites
function bullepop(idd,evt){
var xfenetre,yfenetre,xpage,ypage,element=null;
var offset= 20;           // decalage par defaut
var bulleWidth=200;       // largeur par defaut
var hauteur=50;           // hauteur par defaut
bulleStyle=null;
if (document.layers) {
bulleStyle=document.layers[idd];
xpage = evt.pageX ; ypage  = evt.pageY;
xfenetre = xpage ;yfenetre = ypage ;       
} else if (document.all) {
element=document.all[idd];
xfenetre = evt.x ;yfenetre = evt.y ;
xpage=xfenetre ; ypage=yfenetre    ;   
if (document.body.scrollLeft) xpage = xfenetre + document.body.scrollLeft ;
if (document.body.scrollTop) ypage = yfenetre + document.body.scrollTop;
} else if (document.getElementById) {
element=document.getElementById(idd);
xfenetre = evt.clientX ; yfenetre = evt.clientY ;
xpage=xfenetre ; ypage=yfenetre    ;   
if(evt.pageX) xpage = evt.pageX ;
if(evt.pageY) ypage  = evt.pageY ;
}
if(element)  bulleStyle=element.style;
if(bulleStyle) {
var yp0=ypage;
var yf0=yfenetre;
/* tests incongrus à cause d'Opera5 */
if(bulleStyle.width) bulleWidth = parseFloat(bulleStyle.width);
if(bulleStyle.height) hauteur = parseFloat(bulleStyle.height);
if (xfenetre > bulleWidth+offset) xpage=xpage-bulleWidth-offset;
else {
if (xfenetre >0.5*bulleWidth+offset) xpage=xpage-0.5*bulleWidth-offset;
else xpage=xpage+15;}
if ( yfenetre > hauteur+offset ) ypage=ypage-hauteur-offset;
else ypage=ypage+offset;
if (!bulleStyle.width)    ypage=yfenetre+offset;
if(typeof(bulleStyle.left)=='string') {
bulleStyle.left=xpage+'px'; bulleStyle.top=ypage+'px'; 
} else {
bulleStyle.left=xpage     ; bulleStyle.top=ypage ; }
bulleStyle.visibility="visible";
bulleStyle.zIndex="99";}
}
function couic(){
if(bulleStyle)  bulleStyle.visibility="hidden";
}


 var couleur=Array('#FFEA9E','#F6FFF3','#E6E9FE','#E7D8D1','#D2DED2','#EEE4EE','#C6D4D4','#FFEDF5','#F9FFDB','#D6FFE3','#D8E6FF','#F9E8E8','#FEFFD1','#FFF8DC','FFFAFA','FFFFF0','FFE4E1','D3D3D3','E0FFFF','F0FFF0','E8DADA','F5F5DC','F0FFFF','FFEFD5','F5F5F5','F5FFFA','E6E6FA','F5DEB3','FFF5EE','DCDCDC','E2E0FF','F8F8FF');
function changecoul(){
var dater = new Date();
var jour = dater.getDate();
document.getElementById('bd').style.backgroundColor=couleur[jour];
}


//-->