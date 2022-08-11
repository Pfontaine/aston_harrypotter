from hp_core.sorcier import Sorcier
from hp_core.maison import Maison
from hp_core.categorie_sort import CategorieSort


class Eleve(Sorcier):
    def __init__(self, nom: str, prenom: str, age: int, point_fort: CategorieSort, point_faible: CategorieSort, sorts: list, maison: Maison) -> None:
        super().__init__(nom, prenom, age, point_fort, point_faible, sorts)
        self.__maison = maison

    @property
    def maison(self) -> str:
        return self.__maison

    @maison.setter
    def maison(self, value: Maison) -> None:
        self.__maison = value
    
    def __str__(self) -> str:
        return f"Eleve\n" \
            f"{super().__str__()}" \
            f"Maison: {self.__maison}"

