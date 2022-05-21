class CollectionService:
    def __init__(self):
        self.tab=[]
        
    def Add(self, p):
        self.tab.append(p)

    def Show(self):
        for x in self.tab:
            print(f"Name: {x.name} Age: {x.age}")
