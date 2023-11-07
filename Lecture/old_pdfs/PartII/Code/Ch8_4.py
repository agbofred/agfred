
def rev_quest():
    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f'Dog({self.name},{self.age})'

        def __str__(self):
            return f'{self.name} is {self.age}!'


    A = Dog('Waffles', 6)
    B = Dog('Spot', 8)

    if str(A) == str(B):
        print(A)
    else:
        print(B)


# def class_basic_rev():
class Animal:
    def __init__(self, name, age):
        self._name = name # Politely ask them not to mess with this
        self._age = age

    def __repr__(self):
        return f'Animal({self._name},{self._age})'

    #---

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self.__age = new_age

    def get_name(self):
        return self._name

    def change_name(self, new_name):
        self._name = new_name


a1 = Animal('lion', 26)
a2 = Animal('hyena', 15)

print(a1)
print(a2)
print(a1.get_age())
a1.set_age(8)
print(a1)
# --
#print(a2._Animal__age)

class Human(Animal):
    # New method
    def talk(self):
        return "I am a human."

    # Override method
    def __repr__(self):
        return f'Human({self._name},{self._age})'

H = Human('Jim', 35)
print(H)
print(H.talk())

# if __name__ == '__main__':
    # class_basic_rev()
