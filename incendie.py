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
WIDTH = 1000
HEIGHT = 650
"""DUREE_FEU = 
DUREE_CENDRE = """





################## définition des variables globales #######################
"""Eau 	            Bleu 	   + ∞
   Forêt 	         Vert 	   Dépend des voisins
   Feu 	            Rouge 	Constante DUREE_FEU
   Prairie 	         Jaune 	Dépend des voisins
   Cendres tièdes 	Gris 	   Constante DUREE_CENDRE
   Cendres éteintes 	Noir 	   + ∞"""






################## définition des fonctions (avec docstring) #######################

def generer_terrain():
   pass

def sauver_terrain():
   pass

def charg_terrain():
   pass

def effect_etape():
   pass

def debut_simulation():
   pass

def arret_simulation():
   pass






################## définition des widgets ##################

terrain = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")


generer_Terrain = tk.Button(root, command=generer_terrain, text="Générer un terrain", font=("Times", "10", "bold"), relief="ridge", bd=5)
sauver_Terrain = tk.Button(root, command=sauver_terrain, text="Sauvegarder l'état du terrain", font=("Times", "10", "bold"), relief="ridge", bd=5)
charger_Terrain = tk.Button(root, command=charg_terrain, text="Charger un terrain", font=("Times", "10", "bold"), relief="ridge", bd=5)
effectuer_Etape = tk.Button(root, command=effect_etape, text="Effectuer une étape", font=("Times", "10", "bold"), relief="ridge", bd=5)
demarrer_Simulation = tk.Button(root, command=debut_simulation, text="Démarrer la simulation", font=("Times", "10", "bold"), relief="ridge", bd=5)
arreter_Simulation = tk.Button(root, command=arret_simulation, text="Arrêter la simulation",font=("Times", "10", "bold"), relief="ridge", bd=5)

###cadrillage#######################################################
for i in range(0, WIDTH, 25):
   for j in range(0, HEIGHT, 25):
      terrain.create_rectangle((i,j), (i+25, j+25), outline="black")
####################################################################






################## événements liés aux widgets et appel à la boule de gestion des événements #######################

terrain.grid(column=1, columnspan=2, row=0, rowspan=3)
generer_Terrain.grid(column=0, row=0)
sauver_Terrain.grid(column=0, row=1)
charger_Terrain.grid(column=0, row=2)
effectuer_Etape.grid(column=3, row=1)
demarrer_Simulation.grid(column=1, row=3)
arreter_Simulation.grid(column=2, row=3)






root.mainloop()