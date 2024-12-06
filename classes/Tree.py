"""
28/11/2024

Implémenter sous la forme d'une class un arbre binaire avec les opérations suivantes : 
 - Parcours en profondeur --> avec priorité à gauche --> avec une méthode itérative -> 2, 20, 24,25, 31, 47
 - Parcours en largeur --> avec priorité à droite --> avec une méthode itérative -> 2, 25, 20, 47, 31, 24
 
 
Afficher la taille de l'arbre --> avec une méthode récusive -> 6
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
[Astuce] Récursive est un méthode qui se rappel (elle même)
[Astuce] Avec les méthodes récursives, pensez aux conditions de sorties !
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

    def breadthFirst(self) :
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
    
    def sum(self, node: TreeNode) :       
        if node == None:
            return 0
                
        return node.data + self.sum(node.right) + self.sum(node.left)
    
    def size(self, node: TreeNode) :
        if node == None:
            return 0
        
        return 1 + self.size(node.right) + self.size(node.left)

    
    def insert(self, value, root: TreeNode) :
        if root == None : 
            return TreeNode(value)

        # TODO définir une condition 
        root.left = self.insert(value, root.left)
            
        # root.right = self.insert(value, root.right)

        return root
    
    def search(self, value, root : TreeNode) :
        if root == None : 
            return False
    
        return (root.data == value 
                or self.search(value, root.left) 
                or self.search(value, root.right))
    

class BinarySearchTree: 
    def __init__(self, root: TreeNode) :
        self.root = root

    def insert(self, value, root: TreeNode) :
        if root == None : 
            return TreeNode(value)

        if value < root.data :
            root.left = self.insert(value, root.left)

        if value >= root.data :
            root.right = self.insert(value, root.right)

        return root

#   def inOrder(self, root: TreeNode) :
#         if root == None :
#             return         
        
#         self.inOrder(root.left)
#         print(root.data)
#         self.inOrder(root.right) 

#         return root

    def inOrder(self, root: TreeNode, rightOrder = False) :
        if root == None :
            return []        
        
        left = self.inOrder(root.left, rightOrder)
        right = self.inOrder(root.right, rightOrder) 

        if rightOrder : 
            return [*right, root.data, *left]
        
        return [*left, root.data, *right]    
    
    def search(self, value,  root : TreeNode) :
        if root == None : 
            return False
    
        if root.data == value :
            return True
    
        if value < root.data :
            return self.search(value, root.left) 
   
        if value >= root.data :
            return self.search(value, root.right) 


    
