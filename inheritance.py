class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.speak())
print(cat.speak())

# Polymorphism
animals = [Dog("Buddy"), Cat("Kitty")]

for animal in animals:
    print(animal.speak())
