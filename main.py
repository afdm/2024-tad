# Implémentation d'une pile en programmation procédurale
 
# p = []

# def empiler(p: list, el):
#     p.append(el)

# def depiler(p: list):
#     if estVide(p) :
#         print("La pile est vide")
#         return
    
#     return p.pop()

# def estVide(p: list):
#     return len(p) == 0

# def sommet(p: list):
#     if estVide(p) :
#         print("La pile est vide")
#         return
    
#     return p[-1]


# Implémentation d'une file en programation procédurale

# file = []

# def defiler(file: list) : 
#     if estVide(file) :
#         return
    
#     return file.pop(0)


# def enfiler(file: list, el) :
#     file.append(el)
    
# def tete(file: list) : 
#     return file[0]
    
# def estVide(file) :
#     return len(file) == 0

# enfiler(file, 1)
# enfiler(file, 5)
# enfiler(file, 2)

# print(tete(file))

# defiler(file)

# print(tete(file))

# defiler(file)
# defiler(file)
# defiler(file)


# Implémentation d'une pile en programation orientée objet
# from classes.Pile import Pile

# Tests de notre pile

# pile = Pile()

# pile.empiler(1)
# pile.empiler(5)
# pile.empiler(8)

# print(pile.sommet())

# pile.depiler()

# print(pile.sommet())

# pile.depiler()
# pile.depiler()
# pile.depiler()
# pile.depiler()

# Implémentation d'une File en programation orientée objet
# from classes.File import File

# Tests de notre file

# file = File()

# file.enfiler(1)
# file.enfiler(5)
# file.enfiler(2)

# print(file.tete())

# file.defiler()

# print(file.tete())

# file.defiler()
# file.defiler()
# file.defiler()


# Implémentation (partielle) d'une Liste chainée en programation orientée objet
# TODO Ajouter: 
# - La recherche d'une donnée
# - (Récupérer un élément à un index...)
  
from classes.Node import Node
from classes.LinkedList import LinkedList

# head = Node("A")
# b = Node("B")
# head.next = b

# #  A -> B
# list = LinkedList(head)
# print(list.length())
# print(list.getData())

# #  A -> B -> D
# list.add("D")
# print(list.getData())

# list.insertAt(1, "C")
# print(list.getData())

# list.insertAt(0, "Début")
# print(list.getData())


# list.insertAt(-1, "Fin")
# print(list.getData())

# list.insertAt(100, "bug, ou pas ?!")
# print(list.getData())


# list.add("...")
# list.displayData()

# list.removeIndex(6)
# list.displayData()


# Utilisation de la pile sur un algorithme
from utils import analyseurSyntaxe

uneExpression = "a+b * [2ea] + {y+(mo *(r)}"
# analyseurSyntaxe(uneExpression)

# Utilisation de la file dans un algorithme
from utils import  binSequenceOf
# binSequenceOf(5)

"""
     2
    / \
   20 25
  /   / \
 24  31 47
"""

from classes.Node import TreeNode
from classes.Tree import BinaryTree

n1 = TreeNode(2)
n2 = TreeNode(20)
n3 = TreeNode(25)
n4 = TreeNode(24)
n5 = TreeNode(31)
n6 = TreeNode(47)

n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6

bt = BinaryTree(n1)

# Calcule et retourne la taille de l'arbre
def size (root: TreeNode):
    if root == None:
        return 0
    
    return 1 + size(root.left) + size(root.left)

# Calcule et retourne la somme des noeuds de l'arbre
def sum(root):
    if root == None:
        return 0
    
    return root.data + sum(root.right) + sum(root.left)

# print(size(bt.root))

# print(bt.sum())
# print(sum(bt.root))

# print(bt.depthFirst())
# print(bt.breadthFirst())


def BT_insert(value, root: TreeNode) :
    if root == None : 
        return TreeNode(value)

    # TODO définir une condition 
    root.left = BT_insert(value, root.left)
        
    # root.right = BT_insert(value, root.right)

    return root

def BST_insert(value, root: TreeNode) :
    if root == None : 
        return TreeNode(value)

    if value < root.data :
        root.left = BST_insert(value, root.left)

    if value >= root.data :
        root.right = BST_insert(value, root.right)

    return root

def BT_search(value, root) :
    if root == None : 
        return False
    
    return (root.data == value 
            or BT_search(value, root.left) 
            or BT_search(value, root.right))

def BST_search(value, root) :
    if root == None : 
        return False
    
    if root.data == value :
        return True
    
    if value < root.data :
        return BST_search(value, root.left) 
   
    if value >= root.data :
        return BST_search(value, root.right) 

root = TreeNode(15)
arr = [10, 20, 8, 18, 23, 25]

for el in arr :
    root = BST_insert(el, root)

bt = BinaryTree(root)
print(bt.depthFirst())

# print(BT_search(11, root))
# print(BST_search(11, root))

import time

start_time = time.time()
print(BT_search(23, root))
print(f"----{time.time() - start_time}-----")


start_time = time.time()
print(BST_search(23, root))
print(f"----{time.time() - start_time}-----")
