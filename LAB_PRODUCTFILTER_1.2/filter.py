# Imports
from enum import Enum
from typing import Literal, Union
from dataclasses import dataclass

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

# Class
class ProductFilter:
    @classmethod
    def filter(cls, items: list[object], filter_by: Union[Enum, dict[Literal["color", "size"], Enum]], mode: Literal["color", "size", "Both"]) -> Union[list[object], list]:
        if (mode == "Both" and type(filter_by) is not dict) or mode != "Both" and type(filter_by) is dict:
            raise ValueError("err")
        results = []

        for item in items:
            if mode != "Both" and getattr(item, mode, None) == filter_by:
                results.append(item)
            elif getattr(item, "color", None) == filter_by.get("color", 1) and getattr(item, "size", None) == filter_by.get("size", 1):
                results.append(item)
        return results

# Runner
if __name__ == "__main__":
    # Runner Imports
    from random import choice, random

    # Runner running
    products = []
    for i in range(100):
        products.append(Item(name=str(random()), color=choice([Color.RED, Color.BLUE, Color.GREEN]), size=choice([Size.LARGE, Size.MEDIUM, Size.SMALL])))
    print(products)

    # Dunno
    result = ProductFilter.filter(items=products, filter_by={"color": Color.BLUE, "size": Size.LARGE}, mode="Both")
    print("\n",result)
