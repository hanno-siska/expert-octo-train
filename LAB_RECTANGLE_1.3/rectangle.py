# Imports
from typing import Union

# Classes
class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height

    def __str__(self) -> str:
        return f"Width: {self.width}, Height: {self.height}"

    def __setattr__(self, name: str, value: int):
        self.__dict__[name] = value

class Square(Rectangle):
    def __init__(self, size: int) -> None:
        super().__init__(size, size)

    def __setattr__(self, name: str, value: int):
        if name in ["width", "height"]:
            for i in ["width", "height"]:
                super().__setattr__(i, value)

# Test Function
def use_shape(shape: Union[Rectangle, Square]) -> None:
    width = shape.width
    shape.height = 10

    print(f"Expected Area: {width * 10}")
    print(f"Actual Area: {shape.area()}")

# Runner
use_shape(shape=Rectangle(2,7))
use_shape(shape=Square(5))
