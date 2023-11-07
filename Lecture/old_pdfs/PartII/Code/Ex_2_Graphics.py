import graphics as g

def rev_q():
    w = g.GraphWin('Test', 400, 400)
    w.setBackground('white')
    c = g.Circle(g.Point(100, 200), 20)
    c.draw(w)
    # c.move(200, 100)
    # c.move(0, 200)
    w.getMouse()
    w.close()

rev_q()
