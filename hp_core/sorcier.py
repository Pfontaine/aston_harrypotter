from __future__ import annotations

import math
import random
from typing import Type

from hp_core.categorie_sort import CategorieSort
from hp_core.personne import Personne
from hp_core.sort import Sort


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

    def tomber(self) -> bool:
        aleatoire = random.randint(1, 100)
        if aleatoire <= 10:
            return True
        else:
            return False

    def lancer_sort(self, sort_a_lancer: Sort, opposant: Type[Sorcier], sort_opposant: Sort):

        if type(sort_opposant) is not Sort or type(sort_a_lancer) is not Sort:
            raise TypeError("Un objet de type Sort doit être fourni")

        if sort_a_lancer.vie > 0:
            return f"{self.nom_complet} lance {sort_a_lancer.nom} et se soigne de {sort_a_lancer.vie}", \
                   sort_a_lancer.vie

        if sort_a_lancer == sort_opposant:
            return f"Les sorts lancés sont identique, rien ne se passe", 0

        if sort_a_lancer.categorie == self.__point_fort and self.__point_fort == opposant.point_fort:
            return f"{self.nom_complet} lance {sort_a_lancer.nom} de catégorie {sort_a_lancer.categorie} mais le " \
                   f"point fort des deux opposants est identique.", 0

        if sort_a_lancer.categorie == opposant.point_faible:
            atk = sort_a_lancer.degats * 2
            return f"{self.nom_complet} lance {sort_a_lancer.nom}, c'est très efficace, " \
                   f"{opposant.nom_complet} perd {atk} PV", -atk
        elif sort_a_lancer.categorie == opposant.point_fort:
            atk = math.ceil(sort_a_lancer.degats / 2)
            return f"{self.nom_complet} lance {sort_a_lancer.nom}, ce n'est pas très efficace, " \
                   f"{opposant.nom_complet} perd {atk} PV", -atk
        else:
            return f"{self.nom_complet} lance {sort_a_lancer.nom}, " \
                f"{opposant.nom_complet} perd {sort_a_lancer.degats} PV", -sort_a_lancer.degats

    def __str__(self) -> str:
        return f"{super().__str__()}\n" \
               f"Point fort: {self.__point_fort}\n" \
               f"Point faible: {self.__point_faible}\n"
    