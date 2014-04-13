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
<link rel="stylesheet" type="text/css" href="/static/style.css"/>
<script type="text/javascript" src="/static/programme.js"></script>
</head>
<body>
"""

"""
Fin du fichier HTML.
"""
HTML_footer="""
</body>
</html>
"""
