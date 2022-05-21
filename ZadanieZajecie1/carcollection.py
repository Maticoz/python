from typing import Collection

from collection import Collection


class CarCollection(Collection):
    def Show(self):
        for x in self.tab:
            print(f"===============")
            print(f"Model: {x.model}\nMarka: {x.mark}\nRok produkcji: {x.year}\nPrzebieg: {x.mileage}\n")
            print(f"===============")
