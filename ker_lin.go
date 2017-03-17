package main

import "fmt"
//import "math"

// Trouve le min entre deux entiers
func min(n, m int) int{
	if n < m {
		return n
	} else {
		return m
	}
}

// Trouve le max entre deux entiers
func max(n, m int) int{
	if n < m {
		return m
	} else {
		return n
	}
}

/*
// Clone une matrice
func clone(matrice [][]int, nb_sommets int) [][]int{

	clone := make([][]int, len(matrice))
	
	for i:=0;i<nb_sommets;i++{
		clone[i][j] = matrice[i][j]
	}
	fmt.Println(clone)
return clone	
}

// Permet de sommer les elements d'un vecteur
func sum(matrice []int) int {
  somme := 0
  for i := 0; i < len(matrice); i++ {
    somme += matrice[i]
  }
  return somme
}

// Met des - sur les poids de chaques arrètes d'un même groupe
// Pour l'instant les groupes sont les sommets de 0 à n/2 et de n/2 a n
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
*/

// Regarde si un point appartient a un vecteur
func appartient (vecteur []int, point int) bool{
	for _,v := range vecteur {
		if point==v {
			return true
		}
	}
	return false
}

// Calule de Di pour le sommet i
func calc_di (mat_cout [][]int, groupeI, groupeE []int, temps, i int) int{
	for _,v := range groupeI {
		temps = temps - mat_cout[i][v]
	}
	for _,v := range groupeE {
		temps = temps + mat_cout[i][v]
	}
return temps
}

// Calcule des Di pour chaques sommets
func calc_mat_diff (mat_cout [][]int, groupeI, groupeE []int) []int{

	nb_sommets := len(mat_cout)
	var mat_diff []int

	for i:=0;i<nb_sommets;i++{
		temps := 0
		if appartient(groupeI,i){
			temps = calc_di(mat_cout,groupeI,groupeE,temps,i)
		}else{
			temps = calc_di(mat_cout,groupeE,groupeI,temps,i)
		}
		mat_diff = append(mat_diff,temps)
	}
return mat_diff
}

// Calcul le gain max et retourne les sommets correspondants
func clac_gain(mat_cout [][]int, mat_diff []int) (int, int){

	nb_sommets := len(mat_cout)
	var sommet_a int
	var sommet_b int
	var temps int
	gain := mat_diff[0] + mat_diff[1] - 2*mat_cout[0][1]

	for i:=0;i<nb_sommets;i++{
		for j:=i+1;j<nb_sommets;j++{
			temps = mat_diff[i] + mat_diff[j] - 2*mat_cout[i][j]
			if (max(temps,gain) == temps) {
				gain = temps
				sommet_a = i
				sommet_b = j
			}
		}
	}
return sommet_a, sommet_b
}

// Retirer une composante d'un vecteur
func retirer_point(n int, vecteur []int) []int{

	var vec_nouveau []int
	//vec_nouveau := make([]int, len(vecteur))

	fmt.Println(vecteur)
	for i:=0;i<n;i++{
		vec_nouveau = append(vec_nouveau,vecteur[i])
		fmt.Println(i)
		fmt.Println(vecteur)
		fmt.Println(vecteur[i])
		fmt.Println(vec_nouveau)
	}
	if n <len(vecteur) {
		for i:=n+1;i<len(vecteur);i++{
			vec_nouveau = append(vec_nouveau,vecteur[i])
		}
	}
return vec_nouveau
}

// Retire une ligne d'une matrice
func retirer_ligne(n int, matrice [][]int) [][]int{

	var mat_nouvelle [][]int

	for i:=0;i<n;i++{
		mat_nouvelle = append(mat_nouvelle,matrice[i])
	}
	if n <len(matrice) {
		for i:=n+1;i<len(matrice);i++{
			mat_nouvelle = append(mat_nouvelle,matrice[i])
		}
	}
return mat_nouvelle
}


// Retirer une colonne d'une matrice
func retirer_colonne(n int, matrice [][]int) [][]int{

	mat_nouvelle := make([][]int, len(matrice))

	for i:=0;i<len(matrice);i++{
		for j:=0;j<n;j++{
			mat_nouvelle[i] = append(mat_nouvelle[i],matrice[i][j])
		}
		if n <len(matrice) {
			for j:=n+1;j<=len(matrice);j++{
				mat_nouvelle[i] = append(mat_nouvelle[i],matrice[i][j])
			}
		}
	}
return mat_nouvelle
}

func retirer_un_sommet(n int, matrice [][]int) [][]int{

	var mat_nouvelle [][]int

	mat_nouvelle = retirer_ligne(n,matrice)
	mat_nouvelle = retirer_colonne(n,mat_nouvelle)

return mat_nouvelle
}

// Retirer de la matrice deux sommets
func retirer_deux_sommets(n, p int, mat_cout [][]int) [][]int{
	if max(n,p) == n{
		mat_cout = retirer_un_sommet(n,mat_cout)
		mat_cout = retirer_un_sommet(p,mat_cout)
	} else {
		mat_cout = retirer_un_sommet(p,mat_cout)
		mat_cout = retirer_un_sommet(n,mat_cout)
	}
return mat_cout
}

// Trouve une solution
func trouve_sol(mat_cout [][]int) ([]int,[]int){

	nbsommets := len(mat_cout)
	var groupe1 []int
	var groupe2 []int

	if (nbsommets%2 == 0) {
		for i:=0;i<(nbsommets/2);i++{
			groupe1 = append(groupe1,i)
		}
		for j:=(nbsommets/2);j<nbsommets;j++{
			groupe2 = append(groupe2,j)
		}
	} else {
		for i:=0;i<((nbsommets+1)/2);i++{
			groupe1 = append(groupe1,i)
		}
		for j:=((nbsommets+1)/2);j<nbsommets;j++{
			groupe2 = append(groupe2,j)
		}
	}
return groupe1,groupe2
}

// Redefinition des numeros de sommet pour un groupe
func re_def_un_groupe(leMax,leMin int, groupe []int) []int{

	var new_groupe []int
	var retirer1 int
	var retirer2 int
	existe1 := false
	existe2 := false

	for i:=0;i<len(groupe);i++{
		if (groupe[i] > leMax) && (groupe[i] > leMin) {
			groupe[i] = groupe[i] - 2
		} else if (groupe[i] > leMin) && (groupe[i] == leMax){
			retirer1 = i
			existe1 = true
		} else if (groupe[i] > leMin) && (groupe[i] < leMax) {
			groupe[i] = groupe[i] - 1
		} else if groupe[i] == leMin {
			retirer2 = i
			existe2 = true
		}
	}

	if existe1 {
		new_groupe = retirer_point(retirer1,groupe)
		if existe2 {
			return retirer_point(retirer2,new_groupe)
		}
	} else if existe2 {
		return retirer_point(retirer2,groupe)
	} else {
		return groupe
	}
return groupe
}

// Redefinition des numeros de sommets
func re_def(sommet1,sommet2 int, groupe1, groupe2 []int) ([]int,[]int){

	var new_groupe1 []int
	var new_groupe2 []int
	leMax := max(sommet1,sommet2)
	leMin := min(sommet1,sommet2)

	new_groupe1 = re_def_un_groupe(leMax,leMin,groupe1)
	//fmt.Println(new_groupe1)
	new_groupe2 = re_def_un_groupe(leMax,leMin,groupe2)

return new_groupe1, new_groupe2
}

// Le main
func main() {
	mat_cout := [][]int{
		[]int{0,1,1,0},
		[]int{1,0,1,0},
		[]int{1,1,0,1},
		[]int{0,0,1,0},
	}

	mat_cout_bis := [][]int{
		[]int{0,1,1,0},
		[]int{1,0,1,0},
		[]int{1,1,0,1},
		[]int{0,0,1,0},
	}
	var a int
	var b int
	var groupeI []int
	var groupeE []int
	var mat_diff []int

	groupeI, groupeE = trouve_sol(mat_cout)
	mat_diff = calc_mat_diff(mat_cout_bis,groupeI,groupeE)
	a, b = clac_gain(mat_cout,mat_diff)
	mat_cout = retirer_deux_sommets(a,b,mat_cout)
	groupeI, groupeE = re_def(a,b,groupeI,groupeE)
	//fmt.Println(groupeE)
	//fmt.Println(groupeI)
}
