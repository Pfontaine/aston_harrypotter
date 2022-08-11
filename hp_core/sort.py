from .categorie_sort import CategorieSort

class Sort:
    def __init__(self, nom, couleur, categorie: CategorieSort, degats, vie) -> None:
        self.__nom = nom
        self.__couleur = couleur
        self.__categorie = categorie
        self.__degats = degats
        self.__vie = vie

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def couleur(self):
        return self.__couleur

    @couleur.setter
    def couleur(self, value):
        self.__couleur = value

    @property
    def categorie(self):
        return self.__categorie
    
    @categorie.setter
    def categorie(self, value):
        self.__categorie = value

    @property
    def degats(self):
        return self.__degats

    @degats.setter
    def degats(self, value):
        self.__degats = value

    @property
    def vie(self):
        return self.__vie

    @vie.setter
    def vie(self, value):
        self.__vie = value

    def __str__(self) -> str:
        return f"{self.__nom} - {self.__couleur} - {self.__categorie} - D:{self.__degats} / V:{self.__vie}"