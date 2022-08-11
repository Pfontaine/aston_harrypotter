from enum import Enum


class CategorieSort(Enum):
    ENCHANTEMENT = ("Enchantement")
    MALEDICTION = ("Malediction")
    METAMORPHOSE = ("Métamorphose")
    MALEFICE = ("Maléfice")

    def __init__(self, nom: str) -> None:
        self._nom = nom
    
    @property
    def nom(self) -> str:
        return self._nom

    def __str__(self) -> str:
        return self._nom