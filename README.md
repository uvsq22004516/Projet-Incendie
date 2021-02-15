# Simulation d'incendie - Détails d'utilisation du programme:
#
#       - Règles d'évolution:
#               • Une parcelle d’eau reste une parcelle d’eau durant toute la simulation;
#               • Une parcelle qui devient en feu reste en feu durant la durée DUREE_FEU avant de devenir des cendres tièdes pendant la durée DUREE_CENDRE et enfin devenir des cendres éteintes durant le reste de la simulation; 
#               • Une parcelle de prairie prend feu dès qu’une des 4 cases voisines (gauche, droite, haut, bas) est en feu;
#               • Une parcelle de forêt prend feu avec la probabilité 0.1×nf où nf est le nombre de ses voisins en feu
#
#
#       - Vitesse de la simulation:
#               • Accélérer la vitesse de la simultation: touche "a"
#               • Réduire la vitesse de la simulation: touche "r"
#
#
#       - Différents boutons: 
#               •"NOM_BOUTON" --> bouton qui génère un terrain au hasard avec des parcelles d’eau, de forêt et de prairie
#               •"NOM_BOUTON" --> bouton pour sauvegarder l’état du terrain dans un fichier
#               •"NOM_BOUTON" --> bouton pour charger un terrain depuis un fichier
#               •"NOM_BOUTON" --> bouton qui permet d'effectuer une étape de simulation (raccourci: touche "s")
#               •"NOM_BOUTON" --> bouton qui permet de démarrer une simulation
#               •"NOM_BOUTON" --> bouton pour arrêter la simulation