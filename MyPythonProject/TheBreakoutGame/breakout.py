"""
Name: Hsin-En, Tsai
Date: Dec 13, 2023

stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3		# Number of attempts


def main():
    graphics = BreakoutGraphics(ball_radius=10)
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.ball_out():
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
                graphics.switch = False
            else:
                break
        if graphics.all_brick_remove():
            break
        if graphics.switch:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.bouncing()
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
