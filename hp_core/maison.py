from enum import Enum


class Maison(Enum):
    SERDAIGLE = ("Serdaigle", "bleu")
    POUFSOUFFLE = ("Poufsouffle", "jaune")
    GRYFFONDOR = ("Gryffondor", "rouge")
    SERPENTARD = ("Serpentard", "vert")

    def __init__(self, nom, couleur) -> None:
        self._nom = nom
        self._couleur = couleur

    @property
    def nom(self):
        return self._nom

    @property
    def couleur(self):
        return self._couleur

    def __str__(self) -> str:
        return self._nom + " - " + self._couleur