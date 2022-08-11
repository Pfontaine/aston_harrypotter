class Personne:
    def __init__(self, nom: str, prenom: str, age: int, vie: int) -> None:
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__vie = vie

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, value: str) -> None:
        self.__nom = value

    @property
    def prenom(self) -> str:
        return self.__prenom

    @prenom.setter
    def prenom(self, value: str) -> None:
        self.__prenom = value

    @property
    def nom_complet(self) -> str:
        return f"{self.prenom} {self.nom}"

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        self.__age = value

    @property
    def vie(self) -> int:
        return self.__vie

    @vie.setter
    def vie(self, value: int) -> None:
        self.__vie = value

    def __str__(self) -> str:
        return f"Nom: {self.__nom} {self.__prenom}, Age: {self.__age}, PV: {self.__vie}"
