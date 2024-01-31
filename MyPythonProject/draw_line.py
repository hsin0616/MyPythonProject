"""
File: draw_line
Name: Hsin-En, Tsai
Date: Nov 30, 2023
"""


from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
hole = GOval(SIZE, SIZE)


def main():
    """
    The # time of clicking.
    if n is odd, print a hole.
    if n is even, line hole(n) and hole(n-1). Also, erase the hole(n).
    """
    count = True

    def line(event):
        nonlocal count
        if count:
            window.add(hole, x=event.x - SIZE / 2, y=event.y - SIZE / 2)  # print the hole
            count = False
        else:
            window.remove(hole)
            line = GLine(hole.x + SIZE/2, hole.y + SIZE/2, event.x, event.y)
            window.add(line)
            count = True
    onmouseclicked(line)


if __name__ == "__main__":
    main()