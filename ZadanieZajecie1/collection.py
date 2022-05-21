class Collection:
    def __init__(self, type):
        self.tab    =   []
        self.type   =   type

    def len(self):
        return len(self.tab)

    def checkType(self, p):
        return (type(p) == self.type)

    def checkLen(self, id):
        return (len(self.tab) >= id)

    def Find(self, p):
        id = -1
        for x in self.tab:

            if(x == p):
                break
            ++id
        
        return id
        
    def Add(self, p):
        if(self.checkType(p) == False):
            return print(f'Błedny typ obiektu')

        self.tab.append(p)
        return True

    def Update(self, id, destinationObject):

        if(self.checkLen(id) == False):
            print(f'Błedny numer indexu')
            return False

        if(self.checkType(destinationObject) == False):
            print(f'Błedny typ obiektu')
            return False

        self.tab[id]    =   destinationObject
        return True

    def Delete(self, id):
        if(self.checkLen(id) == False):
            print(f'Błedny numer indexu')
            return False
        del self.tab[id]
        return True
