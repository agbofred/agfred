import graphics as g

def rev_q():
    class Thing:
        def __init__(self, win):
            self.w = win
            cent = g.Point(200,200)
            self.body = g.Circle(cent, 20)
            self.body.draw(self.w)
            self.move(-5)

        def move(self, dx):
            self.body.move(dx, 0)
            self.w.after(1000, self.move, dx)

    w = g.GraphWin('Rev Q', 400, 400)
    w.setBackground('white')
    T = Thing(w)
    click = w.getMouse()
    T.move(5)
    w.getKey()
    w.close()


def testing():
    def add(x,y):
        return x + y

    def test_add():
        assert add(4,5) == 9

    test_add()

testing()
