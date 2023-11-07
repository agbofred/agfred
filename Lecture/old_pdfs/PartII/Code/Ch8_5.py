
def rev_q():
    class Demo:
        def __init__(self):
            self.x = []
        def add(self, v):
            self.x.append(v)
        def get_x(self):
            return self.x

    A, B = Demo(), Demo()
    A.add(3)
    B.add(3)
    C = B.get_x()
    C.append(8)
    print(A.get_x() == B.get_x())


def class_methods():
    class Human(object):
        def __init__(self, age):
            self.age = age
            self.legs = 2

        def __repr__(self):
            return f'Human({self.age})'

    class Pirate(Human):
        def talk(self):
            return "Ayye matey!"

        def __repr__(self):
            return f'Pirate({self.age})'

    class Pegleg(Pirate):
        def __init__(self, age):
            self.age = age
            self.legs = 1
        
        def __repr__(self):
            return f'Pegleg({self.age})'

    class Patch(Pirate):
        # def __init__(self, age):
            # self.age = age
            # self.legs = 2
            # self.eyes = 1
        # Alternate Version
        def __init__(self, age):
            Pirate.__init__(self,age)
            self.eyes = 1

        def __repr__(self):
            return f'Patch({self.age})'



def Ucheck():
    class Job(object):
        def __init__(self, wage):
            self.wage = wage

    class TechJob(Job):
        def __init__(self, wage):
            self.wage = wage
            self.code = True

    class SeniorDev(TechJob):
        def __init__(self, wage, exp):
            TechJob.__init__(self, wage)
            self.exp = exp

    A = SeniorDev(30,10)
    print(dir(A))



def multi_inh():
    class Pirate(object):
        def __init__(self, age):
            self.plunders = True
            self.age = age
            self.eats = 'food'

    class Zombie(object):
        def __init__(self):
            self.type = 'Undead'
            self.eats = 'Brains'

    class Barbosa(Pirate, Zombie):
        def __init__(self, age):
            Zombie.__init__(self)
            Pirate.__init__(self, age)
            self.hates_Jack = True

    B = Barbosa(55)
    print(B.eats)
    print(dir(B))


if __name__ == '__main__':
    rev_q()
    

