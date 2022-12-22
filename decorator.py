from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Animal(Creature):
    def feed(self):
        print("I eat grass")

    def move(self):
        print("I walk forward")


class Decorator(Creature):
    def __init__(self, obj):
        self.obj = obj
        print('New animal created')

    def feed(self):
        self.obj.feed()

    def move(self):
        self.obj.move()


class Swimming(Decorator):
    def move(self):
        print("I swim")


class Flying(Decorator):
    def move(self):
        print("I fly")


class Predator(Decorator):
    def feed(self):
        print("I eat other animals")

if __name__ == "__main__":
    animal = Animal()
    animal.feed()
    animal.move()
    print()
    animal = Swimming(animal)
    animal.feed()
    animal.move()
    print()
    animal = Flying(animal)
    animal.feed()
    animal.move()
    print()
    animal = Predator(animal)
    animal.feed()
    animal.move()
    print()
    animal = Swimming(animal)
    animal.feed()
    animal.move()
    print()