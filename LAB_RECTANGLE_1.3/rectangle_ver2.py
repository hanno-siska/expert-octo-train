# Imports
from typing import Union

# Classes
class Shape:
    def area(self) -> int:
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height

    def __str__(self) -> str:
        return f"Width: {self.width}, Height: {self.height}"

class Square(Shape):
    def __init__(self, size: int):
        self.size = size

    def __str__(self) -> str:
        return f"Width: {self.size}, Height: {self.size}"

    def area(self) -> int:
        return self.size * self.size

# Test Function
r = Rectangle(2, 3)
s = Square(5)

print(r)
print(s)

print(f"Rectangle area: {r.area()}")
print(f"Square area: {s.area()}")
