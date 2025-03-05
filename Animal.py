class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print(f'{self.name}, каже "Мяу"')

class Dog(Animal):
    def make_sound(self):
        print(f'{self.name}, каже "Гав"')

A = Cat("Рижик")
B = Cat("Пижик")
C = Dog("Чижик")

for animal in (A, B, C):
    animal.make_sound()