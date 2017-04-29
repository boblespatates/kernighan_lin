# -*- coding: utf-8 -*-

import numpy as np
import math as m

#Appel de Ker_Lin pour former deux partitions
def Kernighan_Lin(MatriceGraphe):

	#Initialisation des données	
	part_A,part_B = Init_Partition(MatriceGraphe)

	while True:
		vecteur_diff = Calcule_DI(MatriceGraphe,part_A,part_B)
		visiter = []
		non_Visiter = list(range(len(MatriceGraphe)))
		list_Gain = []
		list_Permutation = []

		#On effectue n/2 permutations	
		for i in range(int(m.floor(len(MatriceGraphe)/2))):
			sommet_a,sommet_b,gain = Calc_Gain(MatriceGraphe,vecteur_diff,visiter,part_A,part_B)	
			visiter.append(sommet_a)
			visiter.append(sommet_b)
			non_Visiter.remove(sommet_a)
			non_Visiter.remove(sommet_b)
			list_Gain.append(gain)
			list_Permutation.append([sommet_a,sommet_b])
			
			vecteur_diff = Calc_DI_refresh(MatriceGraphe,sommet_a,sommet_b,part_A,part_B,visiter,vecteur_diff)
		
			Gain_Max,nb_Permutation = Calc_Sum_Gain_Max(list_Gain)
		
		if Gain_Max > 0:
			part_A,part_B = Permuter(part_A,part_B,nb_Permutation,list_Permutation)
		else:
			break
	#print('Partition une:')
	#print(part_A)
	#print('Partition deux:')
	#print(part_B)
	return(part_A, part_B)

#Initialise les partitions
def Init_Partition(MatriceGraphe):
	Taille = len(MatriceGraphe)
	sommet = list(range(Taille))

	if (Taille%2==1):
		return (sommet[:(Taille+1)//2],sommet[(Taille+1)//2:])
	else:
		return (sommet[:Taille//2],sommet[Taille//2:])


#Initialisation de la matrice des differences
def Calcule_DI(MatriceGraphe,part_A,part_B):
	
	vecteur_diff = []
	Taille = len(MatriceGraphe)

	for i in range(Taille):
		
		vecteur_diff.append(0)		

		if part_A.count(i) == 1:
			for j in range(Taille):
				
				if part_A.count(j) == 1:
					vecteur_diff[i] = vecteur_diff[i] - MatriceGraphe[i][j]
				else:
					vecteur_diff[i] = vecteur_diff[i] + MatriceGraphe[i][j]
		else:
			for j in range(Taille):
				
				if part_A.count(j) == 1:	
					vecteur_diff[i] = vecteur_diff[i] + MatriceGraphe[i][j]
				else:
					vecteur_diff[i] = vecteur_diff[i] - MatriceGraphe[i][j]
	return vecteur_diff


#Calucle du gain et retourne les sommets correspondant
def Calc_Gain(MatriceGraphe,vecteur_diff,visiter,part_A,part_B):
	
	#Attention façon très peu propre de faire la chose	
	gain = -100000000

	temps_A,temps_B = Part_Not_Visiter(part_A,part_B,visiter)
	
	for i in temps_A:
		for j in temps_B:
			temps = vecteur_diff[i] + vecteur_diff[j] - 2*MatriceGraphe[i][j]
			if temps > gain:
				gain = temps
				sommet_a = i
				sommet_b = j
	return (sommet_a,sommet_b,gain)


#Trouve les sommets non visite des parties A et B
def Part_Not_Visiter(part_A,part_B,visiter):
	
	new_A = list(part_A)
	new_B = list(part_B)

	for i in visiter:
		if new_A.count(i) == 1:
			new_A.remove(i)
		if new_B.count(i) == 1:
			new_B.remove(i)
	return (new_A,new_B)


#Permet de rafraichir les Di
def Calc_DI_refresh(MatriceGraphe,sommet_a,sommet_b,part_A,part_B,visiter,vecteur_diff):
	
	Taille = len(MatriceGraphe)

	for i in range(Taille):
		if visiter.count(i) == 0:
			if part_A.count(i) == 1: 
				vecteur_diff[i] = vecteur_diff[i] + 2*MatriceGraphe[sommet_a][i] - 2*MatriceGraphe[sommet_b][i]
			else:
				
				vecteur_diff[i] = vecteur_diff[i] + 2*MatriceGraphe[sommet_b][i] - 2*MatriceGraphe[sommet_a][i]
	
	return vecteur_diff


#Permet de trouver le maximum atteind par la somme des gain
def Calc_Sum_Gain_Max(list_Gain):
	
	Gain = 0
	nb_Permutation = 0

	for i in range(len(list_Gain)):
		temps= 0

		for j in list_Gain[:i+1]:
			temps = temps + j
		
		if temps > Gain:
			Gain = temps
			nb_Permutation = i+1
	return (Gain,nb_Permutation) 


#Effectue toutes les permutations pour obtenir les deux sous graphes
def Permuter(part_A,part_B,nb_Permutation,list_Permutation):

	for i in range(nb_Permutation):
		part_A.append(list_Permutation[i][1])
		part_A.remove(list_Permutation[i][0])
		part_B.append(list_Permutation[i][0])
		part_B.remove(list_Permutation[i][1])
	
	return (part_A,part_B)
	
	
Matrice_Graphes = [[0,1,0,0,1,1,0,0],[1,0,0,0,1,1,0,0],[0,0,0,1,0,1,1,1],[0,0,1,0,0,0,1,1],[1,1,0,0,0,1,0,0],[1,1,1,0,1,0,0,0],[0,0,1,1,0,0,0,1],[0,0,1,1,0,0,1,0]]
A = Kernighan_Lin(Matrice_Graphes)
print(A)