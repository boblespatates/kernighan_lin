# -*- coding: utf-8 -*-

import numpy as np


#Appelle de Ker_Lin pour former deux partitions
def Kernighan_Lin(Matrice_graphe):

	#Initialisation des données	
	part_A,part_B,paire = Init_Partition(Matrice_Graphe)
	vecteur_diff = Calcule_DI(Matrice_Graphe,part_A,part_B,paire)
	
	visiter = []
	non_Visiter = range(len(Matrice_graphe))
	sommet_a,sommet_b,gain = Calc_Gain(Matrice_Graphe,vecteur_diff)
	visiter.append(sommet_a)
	visiter.append(sommet_b)
	non_Visiter.remove(sommet_a)
	non_Visiter.remove(sommet_b)

	

#Initialise les partitions
def Init_Partition(Matrice_Graphe):
	
	Taille = len(Matrice_Graphe)
	sommet = range(Taille)

	if (Taille%2==1):
		return (sommet[:(Taille+1)/2],sommet[(Taille+1)/2:],False)
	else:
		return (sommet[:Taille/2],sommet[Taille/2:],True)


#Initialisation de la matrice des differences
def Calcule_DI(Matrice_Graphe,part_A,part_B,paire):
	
	vecteur_diff = []
	Taille_A = len(part_A)
	Taille_B = len(part_B)

	for i in range(len(Matrice_Graphe)):
		
		vecteur_diff.append(0)		

		if i<Taille_A:
			for j in range(Taille_A):
				vecteur_diff[i] = vecteur_diff[i] - Matrice_Graphe[i][j]
			for j in range(Taille_A,Taille_A+Taille_B):
				vecteur_diff[i] = vecteur_diff[i] + Matrice_Graphe[i][j]
		else:
			for j in range(Taille_A):
				vecteur_diff[i] = vecteur_diff[i] + Matrice_Graphe[i][j]
			for j in range(Taille_A,Taille_A+Taille_B):
				vecteur_diff[i] = vecteur_diff[i] - Matrice_Graphe[i][j]
	return vecteur_diff


#Calucle du gain et retourne les sommets correspondant
def Calc_Gain(Matrice_Graphe,vecteur_diff):
	
	Taille = len(Matrice_Graphe)
	gain = vecteur_diff[0] + vecteur_diff[1] - 2*Matrice_Graphe[0][1]

	for i in range(Taille):
		for j in range(i+1,Taille):
			temps = vecteur_diff[i] + vecteur_diff[j] - 2*Matrice_Graphe[i][j]
			if (max([gain,temps]) == temps):
				gain = temps
				sommet_a = i
				sommet_b = j
	return (sommet_a,sommet_b,gain)


#Permet de rafraichir les Di
def Calc_DI_refresh(Matrice_Graphe,sommet_a,sommet_b,part_A,part_B,visiter,vecteur_diff):
	
	Taille = len(Matrice_Graphe)

	for i in range(Taille):
		if visiter.count(i) == 0:
			if part_A.count(i) == 1: 
				vecteur_diff[i] = vecteur_diff[i] + 2*Matrice_Graphe[sommet_a][i] - 2*Matrice_Graphe[sommet_b][i]
			else:
				
				vecteur_diff[i] = vecteur_diff[i] + 2*Matrice_Graphe[sommet_b][i] - 2*Matrice_Graphe[sommet_a][i]

	return vecteur_diff


Matrice_Graphe = [[0,1,1,0,1],[1,0,1,0,1],[1,1,0,1,1],[0,0,1,0,1],[1,1,1,1,0]]
Kernighan_Lin(Matrice_Graphe)
