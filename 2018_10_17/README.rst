Calcul formel, création d'un module, test
=========================================

Calcul formel
-------------

C.f. le sujet de TD

Remarques : 
    * Il faut éviter le copier/coller d'une classe à l'autre.

    * On peut commencer par écrire une méthode dans une sous classe particulière, tester, et ensuite essayer de généraliser. 

Création d'un module
--------------------

Voir `les notes de cours <https://clade.github.io/InfoFip2018/projets/package.html>`_

* Un module est un fichier python

* Un package est un répertoire contenant un fichier ``__init__.py``, des modules et des packages

* Pour importer un package ou un module, il doit être dans un répertoire de la liste donnée pas ``sys.path``, c'est à dire soit le répertoire courant (``os.getcwd()``), soit un répertoire mis par défaut. Il est possible de rajouter un répertoire manuellement dans cette liste (``sys.path.append(...)``)

* Un package n'est importé qu'une seule fois. Ceci est en particulier valable lors de l'utilisation d'une console. Les modifications de la librairie ne seront pas prises en compte. La console IPython utilisée par spyder essaye de recharger automatiquement les modules, en général cela fonctionne. Mais en cas de doute, le plus simple est de redémarrer la console. 

Tests unitaires
---------------

Voir `les notes de cours <https://clade.github.io/InfoFip2018/projets/test_unitaire.html>`_ et la correction du TD. 

La façon habituelle de lancer les tests est d'aller dans une console et d'exécuter :

    python -m unittest discover
    python -m unittest my_package.test.test_mod1

Il est aussi possible d'exécuter cette commande depuis une console IPython en rajoutant un ``!`` avant. Ce point d'exclamation permet de lancer une commande système depuis IPython : par exemple ``!dir`` (ou ``!ls`` sous linux/mac). 


