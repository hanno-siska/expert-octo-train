# Imports
from math import sqrt
from typing import Union, Callable

# Classes
class HolyMathOrSmth:
    @staticmethod
    def solve_normal(a: float, b: float, c: float) -> float:
        return b*b - 4*a*c

    @staticmethod
    def solve_complex(a: float, b: float, c: float) -> float:
        d = b*b - 4*a*c
        return d if d > 0 else float("NaN")

class OmgMath:
    def __init__(self, use: Callable[[HolyMathOrSmth, float, float, float], float]) -> None:
        self.use = use

    def help_me_solve(self, a: float, b: float, c: float) -> float:
        try:
            square = sqrt(self.use(a,b,c))
        except ValueError as e:
            print(f"Cannot take sqrt from zero or below zero num: {e}")
            return (float("NaN"), float("NaN"))
        return ((-b + square) / 2*a, (-b - square) / 2*a)
    
a = OmgMath(use=HolyMathOrSmth.solve_normal)
print(a.help_me_solve(12, -12, 23))
