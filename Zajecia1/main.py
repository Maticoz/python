import person
from collectionservice import CollectionService
from saveservice import SaveService


def main():
    
    '''name    =   input('Name: ')
    age     =   int(input('Age: '))

    p       =   person.Person(name, age)

    SaveService.save("data.txt", p)
    output  =   (f"Imie: {p.name}\nWiek: {p.age}")
    print(output)'''
    

    #x       =   SaveService.load("data.txt")

    p1      =  person.Person("Jan",20)
    p2      =  person.Person("Nowak", 21)


    cs       =  CollectionService()
    cs.Add(p1)
    cs.Add(p2)
    cs.Show()

if __name__ == "__main__":
        main()
