from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def material(self):
        pass

class Suit(Clothes):
    height: int

    def __init__(self, height):
        self.height = height

    @property
    def material(self):
        return 2 * self.height + .3

class Coat(Clothes):
    size: int

    def __init__(self, size):
        self.size = size

    @property
    def material(self):
        return self.size / 6.5 + .5

suit = Suit(182)
coat = Coat(54)

print(suit.material)
print(coat.material)