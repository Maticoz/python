from car import Car
from carcollection import CarCollection
from serialization import Serialization


def main():
    # Wykonanie Marek Derela / 51147 INiN6_PR1.1

    '''
    car1            =   Car("Audi", "A3", 1999, 150000.2)
    car2            =   Car("VW", "B5", 1995, 790000.9)
    car3            =   Car("BMW", "E36", 1992, 230000.5)
    car4            =   Car("Opel", "Astra G", 1991, 165100.3)
    car5            =   Car("Toyota", "Aygo", 2003, 143200.7)

    carCollection   =   CarCollection(type(car1))

    carCollection.Add(car1)
    carCollection.Add(car2)
    carCollection.Add(car3)
    carCollection.Add(car4)
    carCollection.Add(car5)

    print(f"Dlugosc tablicy: {carCollection.len()}")
    carCollection.Delete(carCollection.Find(car3))
    print(f"Dlugosc tablicy: {carCollection.len()}")


    carCollection.Show()
    car4.mileage = 10000.0
    carCollection.Update(carCollection.Find(car4), car4)
    carCollection.Show()

    Serialization.write("cars.bin", carCollection)'''

    carCollectionFromLoad   =   Serialization.load("cars.bin")
    print(f"Dane załadowane z pliku: ")
    carCollectionFromLoad.Show()


if __name__ == "__main__":
        main()
