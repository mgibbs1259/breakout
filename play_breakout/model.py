# model.py
# Allie Meng (awm79) and Mary Gibbs (meg297)
# 5/7/14


"""Model module for Breakout. This module contains the model classes for
Breakout. Instances of model store the paddle, ball, and bricks.The model has
methods for resolving collisions between the various game objects. A lot of your
work on this assignment will be in this class. This module also has an
additional class for the ball. You may wish to add more classes, such as a brick
class, to add new features to the game. What you add is up to you."""


from constants import *
from game2d import *
import random


class Model(object):
    """An instance is a single game of Breakout. The model keeps track of the
    state of the game. It tracks the location of the ball, paddle, and bricks.
    It determines whether the player has won or lost the game.

    Instance Attributes:

        background: The background image displayed during a game. [GImage].

        ball: The ball utilized during a game. [None or Ball()].

        bricks: The bricks remaining during a game. [Empty list or list of
        GRectangle].

        bricksdestroyed: The number of bricks destroyed during a game. [int].

        bricksmessage: The message displayed after a brick is destroyed during
        a game. [None or GLabel].

        lives: The number of lives during a game. [int].

        livescounter: The display of the current number of lives remaining
        during a game. [GLabel].

        paddle: The paddle utilized during a game. [GRectangle].

        score: The value of score during a game. [int].

        scorecounter: The display of the current score during a game.
        [GLabel]."""

    def __init__(self):
        self.background = GImage(source = BACKGROUND_SOURCE, width = GAME_WIDTH,
        height = GAME_HEIGHT, center_x = GAME_WIDTH/2, center_y = GAME_HEIGHT/2)

        self.ball = None

        self.bricks = self.createbricks()

        self.bricksdestroyed = 0

        self.bricksmessage = None

        self.lives = 3

        self.livescounter = GLabel(text = 'SHOT GLASSES = ' + str(self.lives),
        font_name = FONT, font_size = COUNTER_FONTSIZE,
        linecolor = COUNTER_LINECOLOR, x = 105, y = COUNTER_Y, halign = 'left',
        valign = 'middle')

        self.paddle = GRectangle(center_x = GAME_WIDTH/2, y = PADDLE_OFFSET,
        width = PADDLE_WIDTH, height = PADDLE_HEIGHT,
        linecolor = PADDLE_LINECOLOR, fillcolor = PADDLE_FILLCOLOR)

        self.score = 0.00

        self.scorecounter = GLabel(text = 'BAC = ' + str(self.score),
        font_name = FONT, font_size = COUNTER_FONTSIZE,
        linecolor = COUNTER_LINECOLOR, x = 15, y = COUNTER_Y, halign = 'left',
        valign = 'middle')


    def createbricks(self):
        """Creates the bricks that will be utilized during a game. Returns a
        list of GRectangle."""
        bricks = [ ]
        for columnnumber in range(0, BRICKS_IN_ROW):
            colorlist = BRICK_COLORS[1:]
            x = (BRICK_SEP_H/2 + columnnumber*BRICK_WIDTH +
            columnnumber*BRICK_SEP_H)
            newbrickx = GRectangle(x = x, y = GAME_HEIGHT - BRICK_Y_OFFSET,
            width = BRICK_WIDTH, height = BRICK_HEIGHT,
            linecolor = colorlist[0], fillcolor = BRICK_FILLCOLOR)
            bricks.append(newbrickx)
            for rownumber in range(1, BRICK_ROWS):
                y = (GAME_HEIGHT - BRICK_Y_OFFSET - rownumber*BRICK_HEIGHT -
                rownumber*BRICK_SEP_V)
                newbricky = GRectangle(x = x, y = y, width = BRICK_WIDTH,
                height = BRICK_HEIGHT, linecolor = colorlist[0],
                fillcolor = BRICK_FILLCOLOR)
                bricks.append(newbricky)
                colorlist.remove(colorlist[0])
                if colorlist == [ ]:
                    colorlist = BRICK_COLORS[:]
        return bricks


    def createball(self):
        """Creates the ball that will be utilized during a game."""
        self.ball = Ball()


    def collision(self):
        """Returns GObject that has collided with the ball. This method checks
        the four corners of the ball, one at a time. If one of these points
        collides with either the brick or the paddle, it stops checking
        immediately, and returns the object involved in the collision.
        It returns None if no collision occurred."""
        # For the (x, y) coordinate.
        if self.paddle.contains(self.ball.center_x - RADIUS,
        self.ball.center_y - RADIUS):
            return self.paddle
        for brick in self.bricks:
            if brick.contains(self.ball.center_x - RADIUS,
            self.ball.center_y - RADIUS):
                return brick

        # For the (x, y + d) coordinate.
        if self.paddle.contains(self.ball.center_x - RADIUS,
        self.ball.center_y + RADIUS):
            return self.paddle
        for brick in self.bricks:
            if brick.contains(self.ball.center_x - RADIUS,
            self.ball.center_y + RADIUS):
                return brick

        # For the (x + d, y + d) coordinate.
        if self.paddle.contains(self.ball.center_x + RADIUS,
        self.ball.center_y + RADIUS):
            return self.paddle
        for brick in self.bricks:
            if brick.contains(self.ball.center_x + RADIUS,
            self.ball.center_y + RADIUS):
                return brick

        # For the (x + d, y) coordinate.
        if self.paddle.contains(self.ball.center_x + RADIUS,
        self.ball.center_y - RADIUS):
            return self.paddle
        for brick in self.bricks:
            if brick.contains(self.ball.center_x + RADIUS,
            self.ball.center_y - RADIUS):
                return brick

        return None


    def collisionconsequnce(self):
        """Changes the velocity of the ball based on what it has collided
        with during a game. Updates bricksmessage and scorecounter."""
        if ((self.collision() == self.paddle) and (self.ball.center_x + RADIUS <
        self.paddle.center_x - PADDLE_WIDTH/4.0) and (self.ball.vy < 0) or
        (self.collision() == self.paddle) and (self.ball.center_x - RADIUS >
        self.paddle.center_x + PADDLE_WIDTH/4.0) and (self.ball.vy < 0)):
            self.ball.vx = -self.ball.vx

        if ((self.collision() == self.paddle) and (self.ball.center_x - RADIUS >
        self.paddle.center_x - PADDLE_WIDTH) and (self.ball.center_x + RADIUS <
        self.paddle.center_x + PADDLE_WIDTH) and (self.ball.vy < 0)):
            self.ball.vy = -self.ball.vy

        if self.collision() in self.bricks:
            brickhit = self.collision()
            self.bricks.remove(brickhit)
            self.bricksdestroyed += 1
            self.bricksmessage = GLabel(text = 'SHOTS = ' +
            str(self.bricksdestroyed), font_name = FONT,
            font_size = BRICK_HEIGHT, linecolor = COUNTER_LINECOLOR,
            x = brickhit.x + BRICK_WIDTH/2, y = brickhit.y + BRICK_HEIGHT/2,
            halign = "center", valign = "middle")
            self.score += 0.01
            self.scorecounter = GLabel(text = 'BAC = ' + str(self.score),
            font_name = FONT, font_size = COUNTER_FONTSIZE,
            linecolor = COUNTER_LINECOLOR,  x = 15, y = COUNTER_Y,
            halign = 'left', valign = 'middle')
            self.ball.vy = -self.ball.vy


    def loseball(self):
        """The ball disappears if it collides with the bottom of the screen
        during a game. Updates livescounter. Returns True if the ball disappears
        if it collides with the bottom of the screen during a game."""
        movey = self.ball.center_y + self.ball.vy
        if movey + RADIUS <= 0:
            self.ball = None
            self.lives = self.lives - 1
            self.livescounter = GLabel(text = 'SHOT GLASSES = ' +
            str(self.lives), font_name = FONT, font_size = COUNTER_FONTSIZE,
            linecolor = COUNTER_LINECOLOR, x = 105, y = COUNTER_Y, halign = 'left',
            valign = 'middle')
            return True


class Ball(GImage):
    """Instance is a ball. We extend GImage because a ball needs attributes for
    velocity. This subclass adds these two attributes.

    Instance Attributes:

        vx: Velocity in x direction. [int or float].

        vy: Velocity in y direction. [int or float].

    You should add two methods to this class: an initializer to set the
    starting velocity, and a method to "move" the ball. The move method
    should adjust the ball position according to the velocity. NOTE: The ball
    does not have to be a GEllipse. It could be an instance of GImage (Why?).
    This change is allowed, but then you will have to modify the class header up
    above."""

    def __init__(self):
        GImage.__init__(self, source = BALL_SOURCE, width = BALL_DIAMETER,
        height = BALL_DIAMETER, center_x = GAME_WIDTH/2,
        center_y = GAME_HEIGHT/2)
        self.vx = random.uniform(1.0, 5.0)
        self.vx = self.vx*random.choice([-1,1])
        self.vy = -5.0

    def moveball(self):
	"""Moves the ball."""
        movex = self.center_x + self.vx
        movey = self.center_y + self.vy

        if movex + RADIUS > GAME_WIDTH:
            self.center_x = GAME_WIDTH - RADIUS
            self.vx = -self.vx
        else:
            self.center_x += self.vx

        if movex - RADIUS < 0:
            self.center_x = RADIUS
            self.vx = -self.vx
        else:
            self.center_x += self.vx

        if movey + RADIUS > GAME_HEIGHT:
            self.center_y = GAME_HEIGHT - RADIUS
            self.vy= -self.vy
        else:
            self.center_y += self.vy
