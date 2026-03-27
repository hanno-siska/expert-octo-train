# Imports
from dataclasses import dataclass
from random import randint

# Data Class
@dataclass
class SquareInfo:
    normal_square: list[list[int]] = None
    row_square: list[list[int]] = None
    diagonal_square: list[list[int]] = None

    size: int = None

# Classes
class SquareMathIntermediary:
    @staticmethod
    def get_by_row(item: SquareInfo) -> SquareInfo:
        result = []

        for _ in range(item.size):
            for i 
            

class SquareCreatorCore:
    def generate(self, num_range: list[int] = [1,9], size: int = 3) -> SquareInfo:
        result = []

        for _ in range(size):
            intermediary = []
            for _ in range(size):
                intermediary.append(randint(num_range[0], num_range[1]))
            result.append(intermediary)
        return SquareInfo(normal_square=result, size=size)

    def verify_generation(self, item: SquareInfo) -> bool:
        compare_value = 0

        for i, v in enumerate(zip(item.normal_square, item.diagonal_square, item.row_square)):
            value = 0
            for j in v:
                if i == 0:
                    compare_value += j
                value += j
            if value != compare_value:
                return False
        return True

    def math_sys(self, item: SquareInfo) -> SquareInfo: pass

#SquareMathIntermediary.get_by_row(SquareCreatorCore().generate())
done = False
square = SquareCreatorCore()

while not done:
    data = square.generate()
    if square.verify_generation(item=data):
        done = True
        print(data.normal_square)
