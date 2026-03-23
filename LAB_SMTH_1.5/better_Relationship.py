# Imports
from typing import Union
from abc import ABC, abstractmethod

# Data Classes
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

# Parent Classes
class RelationshipBrowser(ABC):
    @abstractmethod
    def find_children(self, parent: str) -> list[str]:
        pass

# Class
class Relationships(RelationshipBrowser):
    def __init__(self) -> None:
        self.relation_data = {}

    def add_child(self, parent: Person, child: Person) -> None:
        search = self.relation_data.get(parent.name)
        if search is not None:
            search.append(child)
        else:
            search = [child,]
        self.relation_data[parent.name] = search

    def find_children(self, parent: str) -> list[Union[str, None]]:
        result = []
        for i in self.relation_data.get(parent, []):
            result.append(i.name)
        return result

class Research:
    def __init__(self, parent: str, relationship: RelationshipBrowser) -> None:
        print(f"{parent} has children: {" ,".join(relationship.find_children(parent))}")

# Testing
parent = Person('John')
parent2 = Person('iggwowgsdf')
child1 = Person('Chris')
child2 = Person('Matt')
child3 = Person('93966469346')

relationships = Relationships()
relationships.add_child(parent, child1)
relationships.add_child(parent, child1)
relationships.add_child(parent2, child3)
print(relationships.relation_data)
Research(parent="iggwowgsdf", relationship=relationships)
