package main

import "fmt"




// Permet de sommer les elements d'un vecteur
func sum(matrice []int) int {
  somme := 0
  for i := 0; i < len(matrice); i++ {
    somme += matrice[i]
  }
  return somme
}

// Met des - sur les poids de chaques arrètes d'un même groupe
func groupe(matrice [][]int, sommet_deb, sommet_fin int) [][]int {
	for i:=sommet_deb;i<sommet_fin;i++{
		for j:=sommet_deb;j<sommet_fin;j++{
			matrice[i][j] = -matrice[i][j]
		}
	}
return matrice
}


// Calcule des Di pour chaque sommets
func calc_mat_diff (mat_cout [][]int) []int{

	nb_sommets := len(mat_cout)
	var mat_diff []int
	temps := mat_cout

	temps = groupe(temps,0,nb_sommets/2)
	temps = groupe(temps,nb_sommets/2,nb_sommets)	
	
	// Somme les lignes de la nouvelle matrice
	for i:=0;i<nb_sommets;i++{
		mat_diff = append(mat_diff, sum(temps[i]))
	}
	
return mat_diff
}
/*
// Calcul du gain
func clac_gain(mat_cout [][]int, mat_diff []int) []int{
			
			
} */

func main() {
	mat_cout := [][]int{
		[]int{0,1,1,0},
		[]int{1,0,1,0},
		[]int{1,1,0,1},
		[]int{0,0,1,0},
	}
	var test []int
	
	test = calc_mat_diff(mat_cout)
	// Affiche les deux graphes
	fmt.Println(test)
}
