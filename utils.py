from classes.Pile import Pile

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

def estUnePaire(symboleOuvrant, symboleFermant) :
    dictionnaire = {
        "]" : "[",
        "}" : "{",
        ")" : "("
    }
    return dictionnaire[symboleFermant] == symboleOuvrant

def analyseurSyntaxe(chaine:str) :
    pile = Pile()

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

"""
Affiche une serie de nombres en binaire de 1 à n

Ex pour n == 5 :

1
10
11
100
101

"""
from classes.File import File

def binSequenceOf(n):
    file = File()
    file.enfiler("1")

    for _ in range(n) :
        tete = file.tete()
        file.enfiler(f"{tete}0")
        file.enfiler(f"{tete}1")

        print(file.defiler())

# Code équivalent

# def binSequenceOf(n) : 
#     file = File()
#     file.enfiler("1")

#     for r in range(n) :
#         el0 = file.tete() + "0"
#         el1 = file.tete() + "1"

#         file.enfiler(el0)
#         file.enfiler(el1)

#         tete = file.defiler()

#         print(tete)


from random import randint, expovariate

def simFileAttente() :    
    file = File()

    class Client: 
        def __init__(self, numero, heureArrivee):
            self.numero = numero
            self.heureArrivee = heureArrivee
            self.dureeDuService = randint(1, 5)

    # Parametres de la simulation en secondes
    dureeMaximumSimulation = 180
    tempsMoyenArriveeClient = 6
    # tempsMoyenServiceClient = 3

    # Etats initiales
    tempsPasse = 0
    nombreDeClientsServis = 0
    tempsAttenteTotal = 0
    prochainneArriveeClient = expovariate(1/tempsMoyenArriveeClient)

    # Simulation
    while tempsPasse < dureeMaximumSimulation :      
        if file.estVide() :
            prochainEvenement = tempsPasse + prochainneArriveeClient
    
        else :
            clientEnTeteDeFile = file.tete()        
            prochainEvenement = min(tempsPasse + prochainneArriveeClient,  tempsPasse + clientEnTeteDeFile.dureeDuService)
            
        # je fais avancer la boucle    
        tempsPasse = prochainEvenement

        if tempsPasse == tempsPasse + prochainneArriveeClient :
            nouveauClient = Client(nombreDeClientsServis+1, tempsPasse)

            file.enfiler(nouveauClient)
            prochainneArriveeClient = expovariate(1 / tempsMoyenArriveeClient)

        else :
            clientServi = file.defiler()
            nombreDeClientsServis +=1             
            
            if(clientServi) : tempsAttenteTotal += tempsPasse - clientServi.heureArrivee
            else : tempsAttenteTotal += tempsPasse

    print("Nombre de clients servis:", nombreDeClientsServis)
    print("Temps d'attente moyen:", tempsAttenteTotal / nombreDeClientsServis)
