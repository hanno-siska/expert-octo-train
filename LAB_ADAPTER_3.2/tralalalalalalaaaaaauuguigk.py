
class Square:
    def __init__(self, side=0):
        self.side = side

    @staticmethod
    def calculate_area(rc):
        return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, obj: object):
        self.width = getattr(obj, "side", 0)
        self.height = getattr(obj, "side", 0)

sq = Square(5)
adapter = SquareToRectangleAdapter(sq)

print(sq.calculate_area(adapter))
