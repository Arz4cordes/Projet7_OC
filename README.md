Projet pour AlgoInvest & Trade
1) Pour utiliser les programmes, installer un environnement virtuel Python,
    par exemple avec la commande python -m venv projet7 sous windows
2) Le fichier requirements.txt contient les bibliothèques à installer.
    pour utiliser les programmes.
3) Le programme bruteforce.py contient l'algorithme "Force brute",
    qui parcourt toutes les combinaisons possibles avec les actions données
    puis qui donne la solution avec:
    * la combinaison qui correspond au plus grand bénéfice
    * le coût total, la recette, et le bénéfice de cette combinaison
    * le temps d'éxécution de l'algorithme
   Lors de l'éxécution du programme, vous avez la possibilité de faire un test
    avec seulement 5 actions au départ, ou bien de lancer l'algorithme pour les 
    20 actions données dans le projet.
   A la fin du programme, vous avez la possibilité de lancer un algorithme qui effectue
    plusieurs calculs de bénéfices, pour un nombre d'actions variant de 12 à 23,
    puis qui affiche le graphique montrant l'évolution du temps d'éxécution de l'algorithme
    "Force Brute" en fonction du nombre d'actions données au départ.
4) Le programme optimized.py contient deux algorithmes optimisés: un algorithme "glouton",
    et un algorithme en "programmation dynamique".
   Lors de l'éxéution du programme, vous avez la possibilité de faire un test
    avec seulement 5 actions au départ, ou bien de lancer l'algorithme qui propose
    une solution avec chacun des deux types d'algorithmes (glouton ou programmation
    dynamique) pour 20 actions, puis pour chacun des deux datasets envoyés par Sienna.
   A la fin du programme, vous avez la possibilité de lancer un algorithme qui effectue
    plusieurs calculs de bénéfices, puis qui affiche le graphique montrant l'évolution
    du temps d'éxécution de l'algorithme optimisé en fonction du nombre d'actions données
    au départ.
