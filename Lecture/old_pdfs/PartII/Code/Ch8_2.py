
def class_initialization():
    class Coordinate:
        def __init__(self,x,y):
            self.x = x
            self.y = y

    A = Coordinate(2,3)
    B = Coordinate(5,4)
    print(f'A.x is {A.x} and A.y is {A.y}')
    print(f'B.x is {B.x} and B.y is {B.y}')


def student_init():
    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            self.is_human = True

    s1 = Student('Bob', 21)
    s2 = Student('Jill', 18)
    s2.is_human = False
    for s in [s1,s2]:
        print(f'{s.name} is {s.age} and {"is" if s.is_human else "is not"} human.')


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

    A = Coordinate(3,4)
    B = Coordinate(1,2)
    O = Coordinate(0,0)

    print(O.distance(A))
    print(A.distance(B))
    print(B.distance(A))


if __name__ == '__main__':
    # class_initialization()
    # student_init()
    coord_methods()
