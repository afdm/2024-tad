class Pile :
    def __init__(self):
        self.elements = []

    def empiler(self, el):
        self.elements.append(el)

    def depiler(self):
        if self.estVide() :
            print("La pile est vide")
            return
        
        return self.elements.pop()

    def estVide(self): 
        return len(self.elements) == 0
    
    def sommet(self):
        if self.estVide() :
            print("La pile est vide")
            return
            
        return self.elements[-1]



class PileFin :
    pass
