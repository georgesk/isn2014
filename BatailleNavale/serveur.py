#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@file serveur.py
Copyright (c) 2014 Georges Khaznadar <georgesk@debian.org>

Ce fichier fait partie du projet Batnav
Batnav est un petit logiciel libre, vous avez le droit de le réutiliser à
votre convenance, dans le respect de la licence GPL V3, ou, selon vos
préférences, de toute version ultérieure de celle-ci.
Le texte de la licence est disponible à http://www.gnu.org/licenses/gpl.html
"""

import cherrypy
import datetime
import os.path
from constantes import HTML_header, HTML_footer
import json

class BatNav:
    """
    cette classe est la définition d'un service web. Les méthodes dont
    l'attribut exposed est Vrai sont autant de pages servies par le serveur
    web.
    """
    def checkSession(self):
        """
        crée un cookie de session si celui-ci n'existe pas encore ;
        enregistre l'heure de début et procède à une authentification,
        si nécesaire.
        """
        if "heure" in cherrypy.session:
            pass
        else:
            cherrypy.session["heure"]=datetime.datetime.now().isoformat();
            raise cherrypy.HTTPRedirect("/login")
    
    @cherrypy.expose
    def index(self):
        """
        page racine du site web.
        @return une page web qui devrait être valide pour le W3C. Cette
        page décrit brièvement le jeu de bataille navale et permet de
        commencer à jouer.
        """
        self.checkSession()
        result=HTML_header.format(title="Bataille navale")
        result+="""
<p>Bonjour {nom} !</p>
<p>Le gestionnaire de bataille navale fonctionne. 
L'adresse où l'automate répond en langue JSON est
<a href='/jeu'>jeu</a>.</p>
<p>
  <a href="http://validator.w3.org/check?uri=referer">
    <img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" />
  </a>
</p>""".format(nom=cherrypy.session["nom"])
        result+=HTML_footer
        return result
    
    @cherrypy.expose
    def login(self, url_retour="/", **dico):
        """
        demande le nom et le stocke dans la session
        @param url_retour est l'URL à servir dès que le nom est défini.
        url_retour est la racine du site par défaut.
        @param dico dictionnaire des paramètres envoyés, par le formulaire,
        ou à partir d'une autre page.
        Si la clé "nom" correspond à une valeur, celle-ci sera utilisée
        pour le login.
        @return un formulaire pour l'authentification si celle-ci n'est
        pas définie dans le dictionnaire dico. Sinon ne renvoie rien : un
        mécanisme d'exception déclenche le service de la page web désignée
        par url_retour.
        """
        if "nom" in dico:
            cherrypy.session["nom"]=dico["nom"]
            if url_retour:
                raise cherrypy.HTTPRedirect(url_retour)
            else:
                return "Bienvenue %s" %dico["nom"]
        else:
            result=HTML_header.format(title="Authentification")
            result+= """
<form>
  <fieldset><legend>Authentification</legend>
    Entrez votre nom : <input type="text" name="nom" />
    <input type="submit" value="OK"/>
  </fieldset>
</form>
"""
            result+=HTML_footer
            return result

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def jeu(self, **dico):
        """
        Cette page sert à renvoyer au format JSON un certain nombre de
        données organisées en dictionnaire Python. La conversion au format
        JSON est faite automatiquement par le module Cherrypy, grâce au
        "décorateur" cherrypy.tools.json_out()
        @param dico le dictionnaire qui rassemble les données entrantes.
        ces données sont celles que la page reçoit.
        @return un objet au format JSON, ses champs doivent être explicites.
        """
        self.checkSession()
        result={}
        result["commentaire"]="Résultat de la page JEU ; les paramètres ne sont pas retravaillés dans cette version de la page"
        result["debut_session"]=cherrypy.session["heure"]
        result["nom"]=cherrypy.session["nom"]
        result["idSession"]=cherrypy.session.id
        result["inputData"]=dico
        return result


"""
définition du répertoire contenant les pages statiques du site web
ces pages n'ont pas besoin d'être calculées.
"""
_STATIC_DIR = os.path.join(os.path.abspath("."), "static")

"""détails de la configuration du serveur."""
dev_config = {
    '/':       {'tools.caching.on': False, # pas de mécanisme de cache
                'tools.sessions.on': True  # gestion des sessions activée
                },
    '/static': {'tools.staticdir.on': True,        # contenu statique
                'tools.staticdir.dir': _STATIC_DIR # dans ce dossier
                },
    }

### bout de code effectué si c'est ce fichier qui est invoqué
### directement, pas chargé comme module par un autre fichier.
if __name__ == '__main__':

    """définition de l'adresse et du port du service web."""
    cherrypy.config.update(
         {'server.socket_host': "localhost",
         'server.socket_port': 8080})


    ### démarrage du serveur web avec la configuration "de développement"
    cherrypy.quickstart(BatNav(), config=dev_config)
