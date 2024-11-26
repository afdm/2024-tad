from .Node import Node

class LinkedList:
    def __init__(self, head: Node) :
        self.head  = head

    def getData(self) -> list :
        # Pointer
        current = self.head
        elements = []

        # Boucle de parcours
        while current :
            elements.append(current.data)
            current = current.next
        
        return elements
    
    def displayData(self) :        
        current = self.head

        data = ""
        while current :                     
            data += str(current.data) + " --> "              
            current = current.next
        print(data)
    
    def length(self) : 
        current = self.head
        counter = 0

        while current :
            counter += 1
            current = current.next

        return counter

    # add data at the end of the list
    def add(self, data) :
        node = Node(data)

        current = self.head
        while current.next :
            current = current.next

        current.next = node

    def insertAt(self, index, data) :
       
        if index < -1 :
            print("Vous pouvez utiliser la méthode add() ou l'index -1 pour inserser à la fin de la liste")
            return

        if index == -1 :
            self.add(data)
            return
        
        if index > self.length() :
            print(f"La liste s'arrête à : {self.length()}")
            return
        
        node =  Node(data)

        if index == 0 :
            node.next = self.head
            self.head = node
            return

        key = 0 
        current = self.head

        while key < index :
            current = current.next
            key += 1

        node.next = current.next
        current.next =  node

    def removeIndex(self, index) :
        if index == 0 :
            self.head = self.head.next
            return

        if index < 0 or index > self.length()-1:
            print(f"index: {index} is out of range")
            return           

        current = self.head
        i = 0

        while i < index :
            previous = current
            current = current.next
            i += 1
        
        previous.next = current.next
        current = previous