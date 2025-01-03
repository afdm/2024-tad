arr = [1, 2, 3, 5, 7] # n
arr2 = [3, 2, 1] #m

for i in arr :
    print(i)

for j in arr2 :
    print(j)

# O(n + m)


for i in arr :
    for j in arr2 :
        print(j + i)
# O(n * m)

for i in arr :
    for j in arr :
        print(j + i)
        print(j + i) # ?
        print(j + i) # ?

# O(n * n) -> O(n^2) 

# Analyse expérimentale
import time
begin = time.time()

for el in arr : # O(n)        
    for el2 in arr : # O(n)
            print(el2 * el)

print(f"{time.time() - begin}s")

def rec_dicho(arr, v) : 
    debut = 0
    fin = len(arr) - 1

    while debut <= fin :
        milieu =  (debut + fin) // 2 # int((debut + fin) / 2)

        if arr[milieu] == v:
            return milieu
        
        # **S2
        if arr[milieu] < v:
            debut = milieu + 1
        
        if arr[milieu] > v:
            fin = milieu - 1

        # **S2 -> code équivalent
        # if tableau[milieu] < valeur:
        #         debut = milieu + 1
        # else:
        #     fin = milieu - 1   

    return -1

print(rec_dicho([1, 2, 3, 5, 7], 5))
# O(log(n)) 

"""
À chaque itération, on divise la taille de la partie du tableau à explorer par deux.
Le nombre d'itérations nécessaires pour trouver l'élément ou déterminer qu'il n'est pas présent est donc proportionnel au logarithme en base 2 de la taille du tableau.
"""