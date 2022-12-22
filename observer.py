from abc import ABC, abstractmethod


class Subject:
    def __init__(self):
        self.observers = set()

    def add(self, observer):
        self.observers.add(observer)

    def remove(self, observer):
        self.observers.remove(observer)

    def update(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class MessageObsOne(Observer):
    def update(self, message):
        print(f"Message One: {message}")


class MessageObsTwo(Observer):
    def update(self, message):
        print(f"Message Two: {message}")


class MessageObsThree(Observer):
    def update(self, message):
        print(f"Message Three: {message}")


if __name__ == "__main__":
    subject = Subject()
    message_One = MessageObsOne()
    message_Two = MessageObsTwo()
    message_Three = MessageObsThree()
    subject.add(message_One)
    subject.update("Hello")
    subject.remove(message_One)
    subject.add(message_Two)
    subject.update("world")
    subject.remove(message_Two)
    subject.add(message_Three)
    subject.update("!")