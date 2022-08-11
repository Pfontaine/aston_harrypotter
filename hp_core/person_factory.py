from .professeur import Professeur
from .maison import Maison
from .categorie_sort import CategorieSort
from .eleve import Eleve
from .hp_util import HPUtil
from .exceptions.sort_error import SortError


class PersonFactory:
    @staticmethod
    def create_eleve(nom: str, prenom: str, age: int, sorts: list,
                     maison: Maison = None, point_fort: CategorieSort = None,
                     point_faible: CategorieSort = None) -> Eleve:
        """
        Crée un élève
        :param nom: Nom de l'élève
        :param prenom: Prénom de l'élève
        :param age: Age de l'élève
        :param sorts: Liste des sorts connus par l'élève
        :param maison: Maison de l'élève
        :param point_fort: Catégorie de sort les mieux maitrisés par l'élève
        :param point_faible: Catégorie de sort pour laquelle l'élève est le plus vulnérable
        :return: Objet élève
        """
        if maison is None:
            maison = HPUtil.choixpeau()

        if point_fort is None:
            point_fort = HPUtil.obtenir_categorie_sort_aleatoire()

        if point_faible is None:
            point_faible = HPUtil.obtenir_categorie_sort_aleatoire()

        if sorts is None:
            raise ValueError("La liste de sort ne peut être None")

        if type(sorts) is not list:
            raise TypeError("Les sorts doivent être donnés sous forme d'un objet list")

        if len(sorts) == 0:
            raise SortError("La liste de sort ne peut pas être vide")

        eleve = Eleve(nom, prenom, age, point_fort, point_faible, sorts, maison)
        return eleve

    @staticmethod
    def create_professeur(nom: str, prenom: str, age: int, sorts: list,
                          point_fort: CategorieSort = None, point_faible: CategorieSort = None) -> Professeur:

        if point_fort is None:
            point_fort = HPUtil.obtenir_categorie_sort_aleatoire()

        if point_faible is None:
            point_faible = HPUtil.obtenir_categorie_sort_aleatoire()

        if sorts is None:
            raise ValueError("La liste de sort ne peut être None")

        if type(sorts) is not list:
            raise TypeError("Les sorts doivent être donnés sous forme d'un objet list")

        if len(sorts) == 0:
            raise SortError("La liste de sort ne peut pas être vide")

        professeur = Professeur(nom, prenom, age, point_fort, point_faible, sorts)
        return professeur
