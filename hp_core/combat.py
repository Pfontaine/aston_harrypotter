import math
import random

from .eleve import Eleve
from .professeur import Professeur


class Combat:
    def __init__(self, eleve: Eleve, professeur: Professeur):
        self.__eleve = eleve
        self.__professeur = professeur
        self.__round = 0
        self.__max_vie_eleve = eleve.vie
        self.__max_vie_professeur = professeur.vie

    @property
    def eleve(self):
        return self.__eleve

    @property
    def professeur(self):
        return self.__professeur

    @property
    def round(self):
        return self.__round

    @property
    def max_vie_eleve(self):
        return self.__max_vie_eleve

    @property
    def max_vie_professeur(self):
        return self.__max_vie_professeur

    def tomber(self) -> bool:
        aleatoire = random.randint(1, 100)
        if aleatoire <= 10:
            return True
        else:
            return False

    def executer_round(self) -> str:
        sort_eleve = self.__eleve.choisir_sort()
        sort_professeur = self.__professeur.choisir_sort()

        self.__round += 1

        if self.tomber():
            return f"{self.__eleve.nom_complet} est tombé et rate son sort"

        if self.tomber():
            return f"{self.__professeur.nom_complet} est tombé et rate son sort"

        if sort_eleve != sort_professeur:
            if sort_professeur.categorie == self.__professeur.point_fort \
                    and sort_professeur.categorie == self.__eleve.point_fort:
                return f"{self.__professeur.nom_complet} lance {sort_professeur}, la catégorie du sort est le point " \
                       f"fort du professeur mais l'élève a le même point fort.\nAucun dégat "

            if sort_eleve.categorie == self.__professeur.point_fort \
                    and sort_eleve.categorie == self.__eleve.point_fort:
                return f"{self.__eleve.nom_complet} lance {sort_eleve}, la catégorie du sort est le point " \
                       f"fort de l'élève mais le professeur a le même point fort.\nAucun dégat "

            texte_a_retourner = ""
            if sort_professeur.categorie == self.__eleve.point_faible:
                atk = sort_professeur.degats * 2
                self.__eleve.vie -= atk
                texte_a_retourner += f"\n{self.__professeur.nom_complet} lance {sort_professeur.nom}, c'est très " \
                                     f"efficace, {self.__eleve.nom_complet} perd {atk}PV "

            if sort_professeur.categorie == self.__eleve.point_fort:
                atk = math.ceil(sort_professeur.degats / 2)
                self.__eleve.vie -= atk
                texte_a_retourner += f"\n{self.__professeur.nom_complet} lance {sort_professeur.nom}, ce n'est pas " \
                                     f"très efficace, {self.__eleve.nom_complet} perd {atk}PV "

            if sort_eleve.categorie == self.__professeur.point_faible:
                atk = sort_eleve.degats * 2
                self.__professeur.vie -= atk
                texte_a_retourner += f"\n{self.__eleve.nom_complet} lance {sort_eleve.nom}, c'est très efficace," \
                                     f" {self.__professeur.nom_complet} perd {atk}PV"

            if sort_eleve.categorie == self.__professeur.point_fort:
                atk = math.ceil(sort_eleve.degats / 2)
                self.__professeur.vie -= atk
                texte_a_retourner += f"\n{self.__eleve.nom_complet} lance {sort_eleve.nom}, ce n'est pas très" \
                                     f" efficace, {self.__professeur.nom_complet} perd {atk}PV "

            return texte_a_retourner
        else:
            return f"{self.__eleve.nom_complet} et {self.__professeur.nom_complet} lance le même sort, rien ne se passe"
