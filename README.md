
# Projet 4 - Développer un programme logiciel en python 
Centre d'échecs 


## Créer un environnement virtuel 

*  Installer la version de Python indiquée sur le repo du projet     
<!-- *  Copier le dossier téléchargé et extrait   -->
*  Depuis le dossier du projet, créer un environnement virtuel : `python -m venv env`     
*  Activer l'environnement virtuel :      
Linux --> `source bin/activate`        
Windows --> `source env/Scripts/activate` (ne pas taper "python" au début de la commande)     
     
L'invite de commande commence maintenant par `(env)`, ce qui signifie qu'on se trouve bien dans l'environnement virtuel. 
A noter que dans l'arborescence de l'IDE, les dossiers et fichiers de travail apparaissent au même niveau que le dossier `env`.     
     
     
## Installer les dépendances 
Taper la commande :     
`pip install -r ./VP-work-220624/requirements.txt` 

## Dossiers de données 

*  Créer un dossier `data` dans le dossier du projet pour toutes les données    
Les données seront stockées dans des fichiers, créés à la volée, portant chacun le nom de la catégorie concernée. 

*  Créer un dossier `images` dans le dossier `data` pour y stocker les images    
Les images seront nommées `<le nom de la catégorie>-<les 10 premiers caractères du titre du livre>.jpg`    


## Arborescence du projet 

VP2-work-220624 (dossier_du_projet) 
 |-- __pycache__ 
 |-- data 
 |-- env 
 |-- one_book.py 
 |-- one_category.py 
 |-- project.py (entrée du script) 


## Lancer le programme 

*  Dans le terminal lancer le script : 
`python ./VP2-work-220624/project.py` 

La console n'affiche aucun retour, pour vérifier que ça fonctionne, il faut ouvrir le dossier `data` pour voir si un fichier `Travel.csv` est créé, puis les suivants. Ouvrir le fichier avec Excel ou LibreOffice pour vérifier son contenu. 



## Tests

Lancer les tests avec Unittest : 
python -m unittest -v <nom_du_fichier_de_test> 

Lancer les tests avec Pytest : 
`pytest` 
Pytest lance tous les tests qu'il trouve. 
Si un fichier commençant par "test" ou "test_" ou finissant apr "_test" est trovué, il ne lancera pas les doctests. 

