def coord_methods():
    class Coordinate:
        def __init__(self,x,y):
            self.x = x
            self.y = y

        def distance(self, other):
            xdiff = (self.x - other.x)
            ydiff = (self.y - other.y)
            dist = (xdiff**2 + ydiff**2)**0.5
            return dist

        def __repr__(self):
            return f'Coordinate({self.x},{self.y})'

        def __str__(self):
            return f'({self.x},{self.y})'

        def __add__(self, other):
            return Coordinate(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Coordinate(self.x - other.x, self.y - other.y)

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __ne__(self, other):
            return not self == other

    A = Coordinate(3,4)
    B = Coordinate(1,2)
    O = Coordinate(0,0)

    print(A)
    print(B)
    print(A+B)
    print(A-B)
    print(A==B)
    print(A!=B)


if __name__ == '__main__':
    coord_methods()
