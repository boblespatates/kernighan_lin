import os
import csv
import math as m

#import des données        
file=open("C:\\users\et\Documents\python\kernighanLin\kernighan_lin\quakes.csv","r")
test=csv.reader(file)

next(test)
lat=[]
long=[]
depth=[]
mag=[]
stations=[]
for row in test:
    lat.append(float(row[1]))
    long.append(float(row[2]))
    depth.append(float(row[3]))
    mag.append(float(row[4]))
    stations.append(float(row[5]))

#création de la matrice d'adjacence
N = 200 #nombre de valeurs à utiliser
matrice = np.zeros((N,N))
for i in range(N):
    for j in range(N):
        matrice[i][j] = m.sqrt( (lat[i]-lat[j])*(lat[i]-lat[j]) * (long[i]-long[j])*(long[i]-long[j]) )

#calcul du résultat
partition = Kernighan_Lin(matrice)

#affichage des résultats
groupe1 = partition[0]
groupe2 = partition[1]

lat1=[]
for i in groupe1:
    lat1.append(lat[i])
    
long1=[]
for i in groupe1:
    long1.append(long[i])
    
lat2=[]
for i in groupe2:
    lat2.append(lat[i])
    
long2=[]
for i in groupe2:
    long2.append(long[i])
    
plt.plot(long1, lat1,"r.")
plt.plot(long2,lat2, "b.")
