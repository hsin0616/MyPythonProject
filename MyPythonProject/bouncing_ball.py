"""
File: bouncing_ball
Name: Hsin-En, Tsai
Date: Dec 1, 2023
"""


from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')

vy = 0

switch = False

def main():
    """
    initial position = (START_X, START_Y)
    ***click an arbitrary position on the window ***
    Bounce to the right side.
    If the ball is not on the window, make the ball be on the original position (START_X, START_Y).
    *** wait for the next clicking ***
    """
    global switch
    times = 1
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    window.add(ball)
    onmouseclicked(bounce)
    while True:
        pause(DELAY)
        while switch and times <= 3:
            vy = 0
            while ball.x < window.width:
                ball.move(VX, vy)
                if ball.y < window.height:
                    pause(DELAY)
                    vy += GRAVITY
                else:
                    vy = vy * REDUCE * (-1)
            window.add(ball, START_X, START_Y)
            times += 1
            switch = False


def bounce(event):
    global switch
    if not switch:
        switch = True


if __name__ == "__main__":
    main()
