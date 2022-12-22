class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


if __name__ == "__main__":
    ex1 = Singleton("Yana", "Gulyaeva")
    ex2 = Singleton("Elena", "Сhemeris")
    print(str(id(ex1)) + "\n" + str(id(ex2)))
    print(ex1 is ex2)