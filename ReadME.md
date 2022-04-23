# Projet 7 : Résolvez des problèmes en utilisant des algorithmes en Python
*par Jean-Corentin Loirat*
le 22/04/2022

Lien du repository git hub : https://github.com/BeanEden/OCR-Projet-7.git

## Description de l'application :
Il s'agit d'algorithmes permettant de calculer la combinaison d'actions financières la plus rentable pour un coût total donné.

Le projet comporte deux algorithmes:
* Un algorithme de force brute (appliqué sur une liste de 20 actions incluse dans le fichier)
* Un algorithe optimisé (applicable sur un fichier csv)

## Utilisation :

### 1 - Créez un environement virtuel dans le dossier de votre choix et activez le :
* Commande terminal : `mkdir projects`
* Commande terminal : `cd projects`
* Commande terminal : `python -m venv env`
* Commande terminal : `env/Scripts/activate.bat` (sous Windows)

### 2 - Importez les packages :
* Commande terminal : `pip install -r requirements.txt`

Importez dans votre environnement virtuel les packages nécessaires au script (tinydb, datetime), tels que présents dans le fichier requirements.txt
Il est possible d'utiliser la ligne de commande "pip install -r requirements.txt",
ou d'installer les packages un par un : "pip install futures3"

### 3 - Lancez les fichiers :
* Commande terminal - Algorithme de force brute : `python bruteforce.py`
* Commande terminal - Algorithme optimisé : `python optimized.py`


## Déroulement

### Algorithme de force brute :
Le script s'exécute seul. Il renvoie le résultat sans intervention de l'utilisateur (la liste à étudier est incluse das le fichier).

Dans le cas où l'utilisateur souhaite exécuter cet algorithme sur une nouvelle liste d'actions, il est possible de le modifier dans le fichier.
La liste doit être une chaîne de caractère de format `"Nom1:prix1:profit1;Nom2:prix2:profit2;..."`


### Algorithme optimisé :
Lors du lancement du script, l'utilisateur choisit:
* le budget total
* le degré de précision
* le fichier csv à étudier

Le script renvoie ensuite le résultat (liste des actions, bénéfice réalisé et temps d'exécution).

En plus de pouvoir indiquer le fichier de notre choix, le script propose directement de lire les fichiers test du projet :
* `.\dataset1_Python+P7.csv`
* `.\dataset2_Python+P7.csv`


## En savoir plus :
Les fonctions et méthodes sont documentées via docstrings avec leurs utilisations, arguments et retours.


## Contenu du repository git hub: 
* bruteforce.py
* optimized.py
* presentation algorithme.pptx
* requirements.txt
