# Imports
from enum import Enum

# Info Classes
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

class Relationship(Enum): # Reaalselt ei näe pointi mitte kuidagi
    PARENT = 1
    CHILD = 2
    SIBLING = 3

# Classes
class Relationships:
    def __init__(self) -> None:
        self.relations = []

    def add_child(self, parent: Person, child: Person) -> None:
        self.relations.append((parent, Relationship.PARENT, child))

class Research:
    def __init__(self, relationships: Relationships) -> None:
        for item in relationships.relations:
            if item[1] == Relationship.PARENT:
                print(f"{item[0].name} has a child called {item[2].name}")

# Test
parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_child(parent, child1)
relationships.add_child(parent, child2)

Research(relationships)