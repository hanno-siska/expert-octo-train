# Imports
from __future__ import annotations
from typing import Any

# Class
class Person:
    def __init__(self) -> None:
        self.name = ""
        self.age = 0

    def __repr__(self) -> str:
        return f"Class: {Person}, name: {self.name}, age: {self.age}"

# Builder Class
class BuildSys:
    def __init__(self):
        self.selected_class = None

    def select(self, cls: object) -> BuildSys:
        self.selected_class = cls()
        return self

    def add_field(self, name: str, value: Any) -> BuildSys:
        self.selected_class.__setattr__(name, value)
        return self

    def build(self) -> object:
        return self.selected_class

cb = BuildSys().select(cls=Person).add_field('name', 'ih').add_field('age', '32').build()
print(cb)
