class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издает звук"


class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит Гав-гав!"


animal = Animal("Животное")
print(animal.speak())

dog = Dog("Барсик")
print(dog.speak())
