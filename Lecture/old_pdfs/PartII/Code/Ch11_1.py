def rev_q():
    class MyClass:
        var1 = 3
        var2 = True

        def __init__(self):
            self.v = self.var1
            if self.var2:
                MyClass.var1 += 1

    A = MyClass()
    B = MyClass()
    MyClass.var2 = False
    C = MyClass()
    print(MyClass.var1)


import matplotlib.pyplot as plt
import string

f = plt.figure()
ax = f.add_axes((.1,.1,.8,.8))  #<--- don't forget to show subplot methods as well!
ax2 = f.add_axes((.2,.6,.2,.2))

ax.plot([0,2,4,8,16],[1,2,3,3,5])
h = ax2.plot([1,2,3,4,5])

ax.set_xticks(range(0,17,4))
ax.set_xticklabels(string.ascii_uppercase[0:5])

ax.set_title('This is an Axes Title')
f.suptitle('This is a Figure Title')

plt.show()

