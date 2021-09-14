class Animal:
    def bark(self):
        print("dog is barking")
class Pets(Animal):
    pass
class Dog(Pets):
    pass
a=Dog()
a.bark()

