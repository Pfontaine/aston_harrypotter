from hp_core import CategorieSort, Sort, Maison, PersonFactory, Combat


def main():
    sorts = [
        Sort("Petrificus Totalus", "Blanc", CategorieSort.MALEFICE, 5, 0),
        Sort("Expeliarmus", "Blanc", CategorieSort.MALEFICE, 5, 0),
        Sort("Vie", "Blanc", CategorieSort.ENCHANTEMENT, 0, 25),
        Sort("Avada Kedavra", "Noir", CategorieSort.MALEFICE, 200, 0),
    ]

    eleve = PersonFactory.create_eleve("Potter", "Harry", 14, sorts, Maison.GRYFFONDOR)
    print(f"{eleve}\n\nVersus\n")
    professeur = PersonFactory.create_professeur("Rogue", "Severus", 50, sorts)
    print(professeur)

    combat = Combat(eleve, professeur)
    while eleve.vie > 0 and professeur.vie > 0:
        print(f"\n\nRound {combat.round + 1}\n---\n")
        print(combat.executer_round())
        print(f"PV {eleve.nom_complet}: {eleve.vie}")
        print(f"PV {professeur.nom_complet}: {professeur.vie}")

    print("FIN COMBAT")


if __name__ == "__main__":
    main()
