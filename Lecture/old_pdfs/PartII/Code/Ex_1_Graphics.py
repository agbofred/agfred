def rev_q():
    import matplotlib.pyplot as plt

    plt.style.use("seaborn-poster")

    f = plt.figure(figsize=(10, 8))
    ax1 = f.add_subplot(224)
    ax2 = f.add_subplot(223)
    ax3 = f.add_subplot(211)

    f.savefig("../Images/RQ13.png")
    plt.show()


def draw_face():
    import graphics as g
    import math

    class Face:
        def __init__(self, win, x, y, r):
            self.w = win
            self.x = x
            self.y = y
            self.r = r
            self.draw_pieces()

        def draw_pieces(self):
            self.face = g.Circle(g.Point(self.x, self.y), self.r)
            self.leye = g.Circle(
                g.Point(self.x - self.r // 3, self.y - self.r // 3), self.r // 4
            )
            self.reye = g.Circle(
                g.Point(self.x + self.r // 3, self.y - self.r // 3), self.r // 4
            )
            self.mouth = g.Polygon(
                [
                    g.Point(
                        self.x + math.cos(a * math.pi / 180) * self.r // 2,
                        self.y + math.sin(a * math.pi / 180) * self.r // 2,
                    )
                    for a in range(20, 161)
                ]
            )

            self.face.setFill("yellow")
            self.leye.setFill("black")
            self.reye.setFill("black")
            self.mouth.setFill("black")

            for obj in [self.face, self.leye, self.reye, self.mouth]:
                obj.draw(self.w)

    w = g.GraphWin("Test", 400, 400)
    w.setBackground("white")
    f1 = Face(w, 200, 200, 70)
    f2 = Face(w, 100, 100, 40)
    w.getMouse()
    w.close()


def move_circ():
    import graphics as g
    import math

    w = g.GraphWin("Circle Motion", 400, 400)
    w.setBackground("white")
    c = g.Circle(g.Point(300, 200), 50)
    c.draw(w)
    for i in range(30):
        w.getMouse()
        dx = c.getCenter().getY() - 200
        dy = c.getCenter().getX() - 200
        c.move(-dx / 10, dy / 10)
    w.close()


def auto_move_circ():
    import graphics as g
    import math

    w = g.GraphWin("Circle Motion", 400, 400)
    w.setBackground("white")
    c = g.Circle(g.Point(300, 200), 50)
    c.draw(w)
    for i in range(300):
        dx = c.getCenter().getY() - 200
        dy = c.getCenter().getX() - 200
        c.move(-dx / 50, dy / 50)
        g.update(30)
    w.close()


def move_face():
    import graphics as g
    import math
    import random

    class Face:
        def __init__(self, win, x, y, r):
            self.w = win
            self.x = x
            self.y = y
            self.r = r
            self.direction = random.choice([-1,1])
            self.draw_pieces()

        def draw_pieces(self):
            self.face = g.Circle(g.Point(self.x, self.y), self.r)
            self.leye = g.Circle(
                g.Point(self.x - self.r // 3, self.y - self.r // 3), self.r // 4
            )
            self.reye = g.Circle(
                g.Point(self.x + self.r // 3, self.y - self.r // 3), self.r // 4
            )
            self.mouth = g.Polygon(
                [
                    g.Point(
                        self.x + math.cos(a * math.pi / 180) * self.r // 2,
                        self.y + math.sin(a * math.pi / 180) * self.r // 2,
                    )
                    for a in range(20, 161)
                ]
            )

            self.face.setFill("yellow")
            self.leye.setFill("black")
            self.reye.setFill("black")
            self.mouth.setFill("black")

            for obj in [self.face, self.leye, self.reye, self.mouth]:
                obj.draw(self.w)

        def orbit(self):
            scale = 50 * self.direction
            dx = -(self.face.getCenter().getY() - 200) / scale
            dy = (self.face.getCenter().getX() - 200) / scale
            for obj in [self.face, self.leye, self.reye, self.mouth]:
                obj.move(dx, dy)
            w.after(30, self.orbit)

    w = g.GraphWin("Test", 400, 400)
    w.setBackground("white")
    fs = [Face(w, random.randint(50,350), random.randint(50,350), random.randint(10,100)) for i in range(10)]
    w.getMouse()
    for f in fs:
        f.orbit()
    key = None
    while key != "q":
        key = w.checkKey()
    w.close()



def control():
    import graphics as g
    class Cart:
        def __init__(self,win, x, y, L, W):
            self.w = win
            self.x = x
            self.y = y
            self.length = L
            self.width = W
            self.key = None
            self.create()

        def create(self):
            self.body = g.Rectangle(
                    g.Point(self.x - self.length //2, self.y - self.width//2),
                    g.Point(self.x + self.length // 2, self.y + self.width//2),
                    )
            self.body.setFill('orange')
            self.body.draw(self.w)

        def control(self):
            if self.key == 'Up':
                self.body.move(0,-10)
            elif self.key == 'Down':
                self.body.move(0,10)
            elif self.key == 'Left':
                self.body.move(-10,0)
            elif self.key == 'Right':
                self.body.move(10,0)
            elif self.key == 'space':
                Bullet(self.w, self.body.getCenter().getX(), self.body.getCenter().getY())

    class Bullet:
        def __init__(self, win, x, y):
            self.w = win
            self.x = x
            self.y = y
            self.create()
            self.move()

        def create(self):
            self.body = g.Circle(g.Point(self.x, self.y), 10)
            self.body.setFill('red')
            self.body.draw(self.w)

        def move(self):
            self.body.move(0,-5)
            w.after(10, self.move)

        
       
    w = g.GraphWin('Test', 800, 800)
    C = Cart(w, 400, 400, 200, 100)
    key = None
    while key != 'q':
        key = w.checkKey()
        C.key = key
        C.control()
        if key:
            print(key)

control()
