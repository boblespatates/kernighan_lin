# -*- coding: utf-8 -*-

import numpy as np


#Appelle de Ker_Lin pour former deux partitions
def Kernighan_Lin(Matrice_graphe):

	#Initialisation des données	
	part_A,part_B,paire = Init_Partition(Matrice_Graphe)
	vecteur_diff = Calcule_DI(Matrice_Graphe,part_A,part_B,paire)


#Initialise les partitions
def Init_Partition(Matrice_Graphe):
	
	Taille = len(Matrice_Graphe)

	if (Taille%2==1):
		return ((Taille+1)/2,(Taille-1)/2,False)
	else:
		return (Taille/2,Taille/2,True)


#Initialisation de la matrice des differences
def Calcule_DI(Matrice_Graphe,part_A,part_B,paire):
	
	vecteur_diff = []	

	for i in range(len(Matrice_Graphe)):
		
		vecteur_diff.append(0)		

		if i<part_A:
			for j in range(part_A):
				vecteur_diff[i] = vecteur_diff[i] - Matrice_Graphe[i][j]
			for j in range(part_A,part_A+part_B):
				vecteur_diff[i] = vecteur_diff[i] + Matrice_Graphe[i][j]
		else:
			for j in range(part_A):
				vecteur_diff[i] = vecteur_diff[i] + Matrice_Graphe[i][j]
			for j in range(part_A,part_A+part_B):
				vecteur_diff[i] = vecteur_diff[i] - Matrice_Graphe[i][j]
	return vecter_diff


#Calucle du gain et retourne le sommets correspondant
def Clac_Gain(Matrice_Graphe,vecteur_diff):
	
	Taille = len(Matrice_Graphe)
	gain = vecteur_diff[0] + vecteur_diff[1] - 2*Matrice_Graphe[0][1]

	for i in range(len(Taille)):
		for j in range(len(Taille)):
			temps = vecteur_diff[i] + vecteur_diff[j] - 2*Matrice_Graphe[i][j]
			if (max([gain,temps]) == temps):
				gain = temps
				sommet_a = i
				sommet_b = j
return (sommet_a,sommet_b)


Matrice_Graphe = [[0,1,1,0,1],[1,0,1,0,1],[1,1,0,1,1],[0,0,1,0,1],[1,1,1,1,0]]
Kernighan_Lin(Matrice_Graphe)
