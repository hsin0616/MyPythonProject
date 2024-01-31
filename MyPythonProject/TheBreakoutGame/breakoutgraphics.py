"""
Name: Hsin-En, Tsai
Date: Dec 13, 2023

stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10       # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

count = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.__dx = 0
        self.__dy = 0
        self.paddle_height = paddle_height
        self.paddle_width = paddle_width
        self.paddle_offset = paddle_offset
        self.count = 0
        self.key_1 = 0
        self.switch = False

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        self.start_x = self.window_width / 2 - ball_radius
        self.start_y = self.window_height / 2 - ball_radius

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window_width - paddle_width) / 2,
                            y=self.window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=self.start_x, y=self.start_y)
        self.ball.filled = True
        self.ball.fill_color = 'slategrey'
        self.ball.color = 'slategrey'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(self.handle_click)
        onmousemoved(self.moving)

        # Draw bricks
        for i in range(0, BRICK_ROWS):
            for j in range(0, BRICK_COLS):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                if j <= 1:
                    self.brick.fill_color = 'black'
                    self.brick.color = 'black'
                elif j <= 3:
                    self.brick.fill_color = 'dimgrey'
                    self.brick.color = 'dimgrey'
                elif j <= 5:
                    self.brick.fill_color = 'grey'
                    self.brick.color = 'grey'
                elif j <= 7:
                    self.brick.fill_color = 'silver'
                    self.brick.color = 'silver'
                elif j <= 9:
                    self.brick.fill_color = 'gainsboro'
                    self.brick.color = 'gainsboro'
                self.window.add(self.brick, x=(brick_spacing+brick_width)*i, y=brick_offset+(brick_spacing+brick_height)*j)

    def handle_click(self, event):
        if not self.switch:
            self.switch = True
            if self.ball.x == self.start_x and self.ball.y == self.start_y:
                self.__dx = random.randint(1, MAX_X_SPEED)
                self.__dy = INITIAL_Y_SPEED
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    def moving(self, event):
        # right out of the window
        if event.x > self.window_width - self.paddle_width / 2:
            self.paddle.x = self.window_width - self.paddle_width
        # left out of the window
        elif event.x - self.paddle_width / 2 < 0:
            self.paddle.x = 0
        # on the window
        else:
            self.paddle.x = event.x - self.paddle_width / 2
            self.paddle.y = self.window_height - self.paddle_offset - self.paddle_height

    def reset_ball(self):
        self.set_ball_position()
        self.window.add(self.ball, self.start_x, self.start_y)

    def set_ball_position(self):
        self.ball.x = self.start_x
        self.ball.y = self.start_y

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def ball_out(self):
        is_ball_out = self.ball.y > self.window.height
        return is_ball_out

    def all_brick_remove(self):
        return self.count == BRICK_ROWS * BRICK_COLS

    def bouncing(self):
        if self.ball.x <= 0 or self.ball.x + BALL_RADIUS * 2 >= self.window_width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

        if (self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS + 1) or
            self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS + 1)) is not None:
            if self.ball.y + 2 * BALL_RADIUS >= self.paddle.y:
                if self.key_1 == 0:
                    self.__dy = -self.__dy
                    self.key_1 = 1
        else:
            self.key_1 = 0
            if self.ball.y < BRICK_OFFSET+(BRICK_SPACING+BRICK_HEIGHT)*BRICK_COLS:
                if (self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y - 1) or
                    self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS + 1)) is not None:
                    self.__dy = -self.__dy
                    if self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y - 1):
                        self.window.remove(self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y - 1))
                        self.count += 1
                    if self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS + 1):
                        self.window.remove(
                            self.window.get_object_at(self.ball.x + BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS + 1))
                        self.count += 1
                if (self.window.get_object_at(self.ball.x - 1, self.ball.y + BALL_RADIUS) or
                    self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS + 1, self.ball.y + BALL_RADIUS)) is not None:
                    if self.window.get_object_at(self.ball.x - 1, self.ball.y + BALL_RADIUS):
                        self.window.remove(self.window.get_object_at(self.ball.x - 1, self.ball.y + BALL_RADIUS))
                        self.count += 1
                    if self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS + 1, self.ball.y + BALL_RADIUS):
                        self.window.remove(self.window.get_object_at(
                            self.ball.x + 2 * BALL_RADIUS + 1, self.ball.y + BALL_RADIUS))
                        self.count += 1
