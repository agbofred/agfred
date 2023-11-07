
from pgl import GWindow, GLine, GRect

PEG_SEP = 3
PEG_ACROSS = 300
PEG_DOWN = 150
DELTA = 332

GWIDTH = PEG_ACROSS * PEG_SEP
GHEIGHT = PEG_DOWN * PEG_SEP

COL_BG = "#272822"
COL_BD = "#a6e22e"
COL_FG = "#ae81ff"

def place_pegs():
    """ Returns a list of points, where the points are tuples. """
    list_pts = []
    for i in range(PEG_ACROSS):
        list_pts.append((i * PEG_SEP, 0))
    for i in range(PEG_DOWN):
        list_pts.append((GWIDTH, i * PEG_SEP))
    for i in range(PEG_ACROSS):
        list_pts.append((GWIDTH - i * PEG_SEP, GHEIGHT))
    for i in range(PEG_DOWN):
        list_pts.append((0, GHEIGHT - i * PEG_SEP))
    return list_pts

def draw_pattern(list_pts, color='black'):
    current_i = 0
    L = len(list_pts)
    finished = False
    while not finished:
        next_i = (current_i + DELTA) % L
        x1, y1 = list_pts[current_i]
        x2, y2 = list_pts[next_i]
        line = GLine(x1, y1, x2, y2)
        line.set_line_width(2)
        line.set_color(color)
        gw.add(line)
        current_i = next_i
        if current_i == 0:
            finished = True

if __name__ == '__main__':
    gw = GWindow(GWIDTH, GHEIGHT)
    bg = GRect(0,0, GWIDTH, GHEIGHT)
    bg.set_line_width(8)
    bg.set_color(COL_BD)
    bg.set_fill_color(COL_BG)
    bg.set_filled(True)
    gw.add(bg)

    

    pegs = place_pegs()
    draw_pattern(pegs, COL_FG)





