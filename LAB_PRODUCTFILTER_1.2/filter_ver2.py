from enum import Enum
from dataclasses import dataclass
from typing import Iterable, Generator

# Enums
class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

class Size(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

# Dataclass
@dataclass
class Item:
    name: str
    color: Color
    size: Size

# Specification base class
class Specification:
    def is_satisfied(self, item: Item) -> bool:
        return False

    def __and__(self, other: "Specification") -> "Specification":
        return AndSpecification(self, other)

# Single attribute specifications
class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Item) -> bool:
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Item) -> bool:
        return item.size == self.size

# Combine multiple specifications
class AndSpecification(Specification):
    def __init__(self, *specs: Specification):
        self.specs = specs

    def is_satisfied(self, item: Item) -> bool:
        return all(spec.is_satisfied(item) for spec in self.specs)

# Filter class
class BetterFilter:
    def filter(self, items: Iterable[Item], spec: Specification) -> Generator[Item, None, None]:
        for item in items:
            if spec.is_satisfied(item):
                yield item

# Runner
if __name__ == "__main__":
    apple = Item("Apple", Color.GREEN, Size.SMALL)
    tree = Item("Tree", Color.GREEN, Size.LARGE)
    house = Item("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]
    bf = BetterFilter()

    print("Green products:")
    green_spec = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green_spec):
        print(f" - {p.name} is green")

    print("\nLarge products:")
    large_spec = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large_spec):
        print(f" - {p.name} is large")

    print("\nLarge blue items:")
    large_blue_spec = large_spec & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue_spec):
        print(f" - {p.name} is large and blue")