"""
@file constantes.py
Copyright (c) 2014 Georges Khaznadar <georgesk@debian.org>

Ce fichier fait partie du projet Batnav
Batnav est un petit logiciel libre, vous avez le droit de le réutiliser à
votre convenance, dans le respect de la licence GPL V3, ou, selon vos
préférences, de toute version ultérieure de celle-ci.
Le texte de la licence est disponible à http://www.gnu.org/licenses/gpl.html
"""

"""
Début du fichier HTML; définit précisément le format utilisé, pour la
conformité à la norme stricte du W3C. Cette chaîne contient un champ à formater
{title}.
"""
HTML_header="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>{title}</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
"""

"""
Fin du fichier HTML.
"""
HTML_footer="""
</body>
</html>
"""

HTML_scriptInit="""
<script src="static/jquery-ui-1.10.4/js/jquery-1.10.2.js"></script>
<script src="static/jquery-ui-1.10.4/js/jquery-ui-1.10.4.js"></script>
<script src="static/jquery-ui-1.10.4/js/jQueryRotate.2.1.js"></script>
<script src="static/js/batnav.js"></script>
<link rel="stylesheet" type="text/css" href="/static/style.css"/>
</head>
<body>
"""

HTML_scriptAuthen="""
<link rel="stylesheet" type="text/css" href="/static/style.css"/>
</head>
<body>
"""

HTML_scriptCombat="""
<script src="static/jquery-ui-1.10.4/js/jquery-1.10.2.js"></script>
<script src="static/jquery-ui-1.10.4/js/jquery-ui-1.10.4.js"></script>
<script src="static/jquery-ui-1.10.4/js/jQueryRotate.2.1.js"></script>
<script src="static/js/Tableau2.js"></script>
<link rel="stylesheet" type="text/css" href="static/style.css"/>
</head>
<body>
"""