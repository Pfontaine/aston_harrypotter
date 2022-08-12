from hp_core.eleve import Eleve
from hp_core.professeur import Professeur
from hp_core.sorcier import Sorcier
from hp_core.sort import Sort


class Combat:
    """
    Classe gérant le combat entre deux personnes
    """
    def __init__(self, eleve: Eleve, professeur: Professeur):
        self.__eleve = eleve
        self.__professeur = professeur
        self.__round = 0
        self.__max_vie_eleve = eleve.vie
        self.__max_vie_professeur = professeur.vie
        self.__attaquant_actuel = self.__eleve

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

    def __tomber(self, sorcier: Sorcier):
        if sorcier.tomber():
            return f"{sorcier.nom_complet} est tombé et rate son sort"

    def executer_round(self) -> str:
        """
        Lance un tour de combat
        :return: Retourne le texte du journal de combat pour ce tour
        """
        sort_eleve = self.__eleve.choisir_sort()
        sort_professeur = self.__professeur.choisir_sort()
        message_a_afficher = ""

        est_au_sol = self.detecter_chute()
        if est_au_sol:
            message_a_afficher += est_au_sol
        else:
            message_a_afficher = self.calculer_vie_joueur(self.__eleve, self.__professeur, sort_eleve, sort_professeur)

        self.__round += 1

        return message_a_afficher

    def detecter_chute(self) -> str | bool:
        """
        Detecte si un des personnages va tomber dans le tour
        :return: Renvoie le texte à ajouter au journal de combat ou False si aucunes des deux personnes n'est tombé
        """
        if self.__eleve.tomber():
            return self.__tomber(self.__eleve)
        elif self.__professeur.tomber():
            return self.__tomber(self.__professeur)
        else:
            return False

    def calculer_vie_joueur(self, eleve: Eleve, professeur: Professeur, sort_eleve: Sort, sort_professeur: Sort) -> str:
        """
        Calcule les nouveaux point de vie des personnes
        :param eleve: Objet représentant l'élève
        :param professeur: Objet représentant le professeur
        :param sort_eleve: Sort qui est lancé par l'élève
        :param sort_professeur: Sort qui est lancé par le professeur
        :return: Renvoi du texte pour le journal de combat
        :todo: Refactoriser
        """
        message = ""
        degat_eleve = eleve.lancer_sort(sort_eleve, professeur, sort_professeur)
        if degat_eleve[1] > 0:
            eleve.vie += degat_eleve[1] if degat_eleve[1] + eleve.vie < self.__max_vie_eleve else self.__max_vie_eleve - eleve.vie
        else:
            professeur.vie += degat_eleve[1]
        message += degat_eleve[0] + "\n"
        degat_professeur = professeur.lancer_sort(sort_professeur, eleve, sort_eleve)
        if degat_professeur[1] > 0:
            professeur.vie += degat_professeur[1] if degat_professeur[1] + professeur.vie < self.__max_vie_professeur else self.__max_vie_professeur - professeur.vie
        else:
            eleve.vie += degat_professeur[1]
        message += degat_professeur[0]

        return message
