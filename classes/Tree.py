"""
28/11/2024

Implémenter sous la forme d'une class un arbre binaire avec les opérations suivantes : 
 - Parcours en profondeur --> avec priorité à gauche --> avec une méthode itérative -> 2, 20, 24,25, 31, 47
 - Parcours en largeur --> avec priorité à droite --> avec une méthode itérative -> 2, 25, 20, 47, 31, 24
 
 
Afficher la taille de l'arbre --> avec une méthode récusive -> 7
Calculer la somme de l'arbre --> avec une méthode récusive -> 149

L'arbre que vous devez représenter est le suivant :
     2
    / \
   20 25
  /   / \
 24  31 47

[Astuce] Utiliser des Noeuds  pour contruire votre arbre binaire.
    - Implémenter la class Noeud d'un arbre 
[Astuce] Attention les piles ont leurs propres sens
[Astuce] Récursive est un methode qui se rappel (elle même)
[Astuce] Avec les methodes récurvives, pensez aux conditions de sortie !
[Astuce] https://github.com/afdm/2024-tad/
"""

from .Node import TreeNode
from .Pile import Pile
from .File import File

class BinaryTree: 
    def __init__(self, root: TreeNode) :
        self.root = root

    def depthFirst(self) :
        data = []
        pile = Pile()
        pile.empiler(self.root)

        while not pile.estVide() :
            current = pile.depiler()
            # print(current.data)
            data.append(current.data)

            if current.right:
                pile.empiler(current.right)

            if current.left:
               pile.empiler(current.left)

        return data

    def breadFirst(self) :
        data = []
        file = File()
        file.enfiler(self.root)

        while not file.estVide() :
            current = file.defiler()
            # print(current.data)
            data.append(current.data)
       
            if current.right:
                file.enfiler(current.right)

            if current.left:
               file.enfiler(current.left)
        
        return data
