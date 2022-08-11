from hp_core.sorcier import Sorcier


class Professeur(Sorcier):
    def __init__(self, nom, prenom, age, point_fort, point_faible, sorts) -> None:
        super().__init__(nom, prenom, age, point_fort, point_faible, sorts)
        self.vie = 150

    def __str__(self):
        return f"Professeur\n{super().__str__()}"
