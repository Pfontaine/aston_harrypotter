import random

from hp_core.categorie_sort import CategorieSort
from hp_core.maison import Maison


class HPUtil:
    """
    Collection de méthodes statique utilitaires
    """
    @staticmethod
    def choixpeau():
        """
        Retourne aléatoirement une maison
        :return: Objet Maison
        """
        maisons = [Maison.GRYFFONDOR, Maison.SERDAIGLE, Maison.POUFSOUFFLE, Maison.SERPENTARD]
        aleatoire = random.randint(0, 3)
        return maisons[aleatoire]

    @staticmethod
    def obtenir_categorie_sort_aleatoire():
        """
        Retourne aléatoirement une catégorie de sort
        :return: Objet CategorieSort
        """
        categorie = [CategorieSort.MALEFICE, CategorieSort.ENCHANTEMENT, CategorieSort.MALEDICTION, CategorieSort.METAMORPHOSE]
        aleatoire = random.randint(0, 3)
        return categorie[aleatoire]



