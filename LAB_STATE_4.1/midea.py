# Imports
from enum import Enum
from typing import Literal

# Classes
class States(Enum):
    UNLOCKED = 0
    LOCKED = 1
    ERR = 2

class CombinationLock:
    def __init__(self, combination: list[int]) -> None:
        self._combination = combination
        self._combination_length = len(self._combination)
        self._state = States.LOCKED

        self.user_combination = []

    def enter_digit(self, num: int) -> None:
        if self._state is not States.LOCKED:
            return None
        self.user_combination.append(num)
        length = len(self.user_combination) - 1
        if length > self._combination_length:
            self._state = States.ERR
        else:
            if self._combination[length] != num:
                self._state = States.ERR
        
        if self._state is not States.ERR and self._combination == self.user_combination:
            self._state = States.UNLOCKED

    def status(self) -> tuple[str, States]:
        return ("".join(list(str(i) for i in self.user_combination)), self._state)

# Main
cl = CombinationLock(combination=[1,2,3,4,5])
answer = [1,2,3,5,5]

for i in answer:
    cl.enter_digit(i)
    print(cl.status())
