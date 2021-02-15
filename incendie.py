################## informations liées au groupe #######################

# groupe DLMP 5
# Gabriel CHAMPENOIS
# Alexis BODEN
# Lucas LEMARECHAL
# Djenna SEDDOUGUI
# Lucien SAVEY
# Alberic BEAUSSANT

# https://github.com/uvsq22004516/projet_incendie

#########################################



################## import des librairies #######################
import tkinter as tk
import random as rd

root = tk.Tk()
root.title("Simulation d'incendie (IN200 - projet n°1)")


################## définition des constantes (en MAJ) #######################
WIDTH = 900
HEIGHT = 600
DUREE_FEU = 0
DUREE_CENDRE = 0

################## définition des variables globales #######################
"""Eau 	            Bleu 	   + ∞
   Forêt 	         Vert 	   Dépend des voisins
   Feu 	            Rouge 	Constante DUREE_FEU
   Prairie 	         Jaune 	Dépend des voisins
   Cendres tièdes 	Gris 	   Constante DUREE_CENDRE
   Cendres éteintes 	Noir 	   + ∞"""


################## définition des fonctions (avec docstring) #######################



################## définition des widgets ##################

terrain = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")




################## événements liés aux widgets et appel à la boule de gestion des événements #######################

terrain.grid()
root.mainloop()