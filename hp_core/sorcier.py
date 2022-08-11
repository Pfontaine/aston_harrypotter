import random

from .categorie_sort import CategorieSort
from .personne import Personne
from .sort import Sort


class Sorcier(Personne):
    def __init__(self, nom: str, prenom: str, age: int, point_fort: CategorieSort, point_faible: CategorieSort,
                 sorts: list) -> None:
        super().__init__(nom, prenom, age, 100)
        self.__point_fort = point_fort
        self.__point_faible = point_faible
        self.__sorts = sorts

    @property
    def point_fort(self) -> CategorieSort:
        return self.__point_fort

    @point_fort.setter
    def point_fort(self, value: CategorieSort) -> None:
        self.__point_fort = value

    @property
    def point_faible(self) -> CategorieSort:
        return self.__point_faible

    @point_faible.setter
    def point_faible(self, value: CategorieSort) -> None:
        self.__point_faible = value

    @property
    def sorts(self) -> list:
        return self.__sorts

    @sorts.setter
    def sorts(self, value: list) -> None:
        self.__sorts = value

    def choisir_sort(self) -> Sort:
        aleatoire = random.randint(0, len(self.__sorts) - 1)
        return self.__sorts[aleatoire]

    def __str__(self) -> str:
        return f"{super().__str__()}\n" \
               f"Point fort: {self.__point_fort}\n" \
               f"Point faible: {self.__point_faible}\n"
    