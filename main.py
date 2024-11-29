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

def size (root: TreeNode):
    if root == None:
        return 0
    
    return 1 + size(root.left) + size(root.left)

def sum(root):
    if root == None:
        return 0
    
    return root.data + sum(root.right) + sum(root.left)

print(size(bt.root))
print(sum(bt.root))

# print(bt.depthFirst())
# print(bt.breadFirst())



