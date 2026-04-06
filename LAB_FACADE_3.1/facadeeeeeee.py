# Imports
from dataclasses import dataclass
from random import randint

@dataclass
class SquareInfo:
    normal_square: list[list[int]] = None
    row_square: list[list[int]] = None
    column_square: list[list[int]] = None
    diagonal_square: list[list[int]] = None
    size: int = None

class SquareMathIntermediary:

    @staticmethod
    def get_rows(item: SquareInfo) -> list[list[int]]:
        return item.normal_square

    @staticmethod
    def get_columns(item: SquareInfo) -> list[list[int]]:
        return [
            [item.normal_square[row][col] for row in range(item.size)]
            for col in range(item.size)
        ]

    @staticmethod
    def get_diagonals(item: SquareInfo) -> list[list[int]]:
        diag1 = [item.normal_square[i][i] for i in range(item.size)]
        diag2 = [item.normal_square[i][item.size - i - 1] for i in range(item.size)]
        return [diag1, diag2]

class Generator:
    def generate(self, num_range: list[int], size: int) -> SquareInfo:
        square = [
            [randint(num_range[0], num_range[1]) for _ in range(size)]
            for _ in range(size)
        ]
        return SquareInfo(normal_square=square, size=size)

class MagicSquareGenerator:
    def build(self, item: SquareInfo) -> SquareInfo:
        item.row_square = SquareMathIntermediary.get_rows(item)
        item.column_square = SquareMathIntermediary.get_columns(item)
        item.diagonal_square = SquareMathIntermediary.get_diagonals(item)
        return item

class Verifier:
    def is_magic(self, item: SquareInfo) -> bool:
        sums = []

        sums.extend(sum(row) for row in item.row_square)

        sums.extend(sum(col) for col in item.column_square)

        sums.extend(sum(diag) for diag in item.diagonal_square)

        return len(set(sums)) == 1

class MagicSquareFacade:
    def __init__(self):
        self.generator = Generator()
        self.builder = MagicSquareGenerator()
        self.verifier = Verifier()

    def create_magic_square(self, size: int = 3, num_range: list[int] = [1, 9]) -> SquareInfo:
        while True:
            square = self.generator.generate(num_range, size)
            square = self.builder.build(square)
            if self.verifier.is_magic(square):
                return square

if __name__ == "__main__":
    facade = MagicSquareFacade()
    result = facade.create_magic_square(size=3, num_range=[1, 6])

    print("Magic Square Found:\n")
    for row in result.normal_square:
        print(row)