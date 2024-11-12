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

# Implémentation d'une pile en programation orientée objet

# Tests de notre pile
# (Faire les tests pour les deux cas)

# from classes.Pile import Pile

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


"""
Problème : Vérifier qu'une expression n'est pas d'erreur de syntaxe. Par exemple, que ==> [({ <=== soient bien refermés

1. Lire / Parcourir la chaine
2. Repérer les symboles ouvrants 
3. Repérer les symboles fermants
4. Il y deux conditions de sortie :
  -> 1) on recontre un symbole ouvrant, il n'est jamais refermé... A la fin de l'opération il reste des informations sur la pile
  -> 2) le symbole fermant ne correspond pas au dernier symbole ouvrant !

Ex : "a+b * [2ea] + {y+(mo *(r)} --> Ceci, a une erreur de syntaxe, il manque une parenthèse (avant le dernier symbole). 
"""

from classes.Pile import Pile

pile = Pile()

dictionnaire = {
    "]" : "[",
    "}" : "{",
    ")" : "("
}

def estUnePaire(symboleOuvrant, symboleFermant) :
    return dictionnaire[symboleFermant] == symboleOuvrant

def analyseur(chaine) :

    # Parcours de la chaine
    for c in chaine :

        # Est-ce que notre caractère est un symbole ouvrant ? 
        if c in ["[", "(", "{"] :
            pile.empiler(c)
        
        # Est-ce que notre caractère est un symbole fermant ? 
        if c in ["]", ")", "}"] :
            dernierSymboleOuvrant = pile.depiler()

            # Si oui, est-ce qu'il forme une paire avec le dernier caractère ouvrant ?
            if not estUnePaire(dernierSymboleOuvrant, c) :
                print("Syntaxe incorrecte")
                return
    
    # Est qu'il reste des éléments sur la pile ? (condition n°1 de sortie)
    if not pile.estVide() :
        print("Syntaxe incorrecte !")
        return
    
    # Si on arrive ici, c'est qu'on a passé toutes les vérifications !
    print("Syntaxe est correcte")


uneExpression = "a+b * [2ea] + {y+(mo *(r)}"

analyseur(uneExpression)