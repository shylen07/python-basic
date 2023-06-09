# Title: Classes and Objects
# Created by Devender Singh

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "barks")

dog = Dog("Buddy")
dog.bark()
