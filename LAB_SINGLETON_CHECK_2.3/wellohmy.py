## LAB2.2
# Class
class Person:
    def __init__(self, identification_number: int, name: str) -> None:
        self.identification_number = identification_number
        self.name = name

class Factory:
    _id = 0

    def create_person(cls, name: str) -> Person:
        cls._id += 1
        return Person(identification_number=cls._id, name=name)


factory = Factory()

p1 = factory.create_person("Anna")
p2 = factory.create_person("Mark")

print(p1.identification_number, p1.name)
print(p2.identification_number, p2.name)


## NEW
def is_dunno(i, k) -> bool:
    if i.__class__ is k.__class__:
        return True
    return False

print(is_dunno(p1, p2))