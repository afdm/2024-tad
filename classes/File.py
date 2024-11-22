class File :
    def __init__(self): 
        self.elements = []

    def enfiler(self, el):
        self.elements.append(el)

    def defiler(self) :
        if self.estVide():
           print("La file est vide")
           return 
        
        return self.elements.pop(0)

    def tete(self):
        if self.estVide():
           print("La file est vide")
           return

        return self.elements[0]

    def estVide(self):
        return len(self.elements) == 0
