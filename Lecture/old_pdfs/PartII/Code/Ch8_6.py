
def rev_q():
    class ObjA:
        def __init__(self):
            self.x = 5

    class ObjB(ObjA):
        def __init__(self):
            ObjA.__init__(self)
            self.x = 8

    class ObjC(ObjB):
        def __init__(self):
            ObjA.__init__(self)
            self.y = self.x + 2

    class ObjD(ObjC):
        def __init__(self):
            ObjC.__init__(self)
            ObjB.__init__(self)
            self.x += self.y

    D = ObjD()
    print(D.x)

def multi_inh():
    class Pirate(object):
        def __init__(self, age):
            self.plunders = True
            self.age = age
            self.eats = 'food'

        def talk(self):
            print('Shiver me timbers!')

    class Zombie(object):
        def __init__(self):
            self.type = 'Undead'
            self.eats = 'Brains'

        def talk(self):
            print('Grrrrrggghh')

    class Barbosa(Pirate, Zombie):
        def __init__(self, age):
            Zombie.__init__(self)
            Pirate.__init__(self, age)
            self.hates_Jack = True

    B = Barbosa(55)
    print(B.eats)
    print(dir(B))

def basic_class_var():
    class MyBestClass:
        a_class_variable = 'Hello!'

        def __init__(self):
            self.a_instance_variable = 'Hi!'

    print(MyBestClass.a_class_variable)
    A = MyBestClass()
    print(A.a_class_variable)

    # Changing
    B = MyBestClass()
    A.a_class_variable = 'Oh hi!'
    print(A.a_class_variable, B.a_class_variable)


class Checker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_move(self):
        pass

    def move(self):
        pass

    def jump(self):
        pass

class RedChecker(Checker):
    color = 'red'
    count = 0

    def __init__(self, x, y):
        Checker.__init__(self, x,y)
        self.direction = 'Up'
        RedChecker.count += 1

    def __del__(self):
        RedChecker.count -= 1


if __name__ == '__main__':
    rev_q()
