# constants.py
# Allie Meng (awm79) and Mary Gibbs (meg297)
# 5/7/14


"""Constants for Breakout. This module global constants for the game Breakout.
These constants need to be used in the model, the view, and the controller.
As these are spread across multiple modules, we separate the constants into
their own module. This allows all modules to access them."""


import colormodel
import sys


### WINDOW CONSTANTS (COORDINATES IN PIXELS) ###

# The width of the game display. 
GAME_WIDTH = 680
# The height of the game display.
GAME_HEIGHT = 820


### PADDLE CONSTANTS ###

# The width of the paddle.
PADDLE_WIDTH = 58
# The height of the paddle.
PADDLE_HEIGHT = 11
# The distance of the, bottom of the, paddle from the bottom.
PADDLE_OFFSET = 30
# The color utilized for the paddle during a game.
PADDLE_LINECOLOR = colormodel.CYAN
# The color utilized for the paddle during a game.
PADDLE_FILLCOLOR = colormodel.BLACK 


### BRICK CONSTANTS ###

# The horizontal separation between bricks.
BRICK_SEP_H = 5
# The vertical separation between bricks.
BRICK_SEP_V = 4
# The height of a brick.
BRICK_HEIGHT = 8
# The offset of the top brick row from the top.
BRICK_Y_OFFSET = 70
# The number of bricks per row.
BRICKS_IN_ROW = 10
# The number of rows of bricks, in range 1..10.
BRICK_ROWS = 10
# The width of a brick.
BRICK_WIDTH = GAME_WIDTH/BRICKS_IN_ROW - BRICK_SEP_H
# The color utilized for the bricks during a game.
BRICK_FILLCOLOR = colormodel.BLACK
# The colors utilized for the bricks during a game.
BRICK_COLORS = [colormodel.CYAN, colormodel.CYAN, colormodel.GREEN,
colormodel.GREEN, colormodel.YELLOW, colormodel.YELLOW, colormodel.RED,
colormodel.RED]


### BALL CONSTANTS ###

# The diameter of the ball in pixels.
BALL_DIAMETER = 26
# The radius of the ball in pixels.
RADIUS = BALL_DIAMETER/2.0


### GAME CONSTANTS ###

# The number of attempts in a game.
NUMBER_TURNS = 3
# State before the game has started.
STATE_INACTIVE = 0
# State when we are counting down to the ball serve.
STATE_COUNTDOWN = 1
# State when we are waiting for user to click the mouse.
STATE_PAUSED = 2
# State when the ball is in play and being animated.
STATE_ACTIVE = 3
# State when the game is over.
STATE_COMPLETE = 4


### ADDITIONAL CONSTANTS ###

# The source of the background image displayed during a game.
BACKGROUND_SOURCE = "background.jpg"
# The font utilized for the messages during a game.
FONT = "arialbold.ttf"
# The font sized utilized for the counters during a game.
COUNTER_FONTSIZE = 15
# The color utilized for the counters during a game.
COUNTER_LINECOLOR = colormodel.WHITE
# The y value utilized for the counters during a game.
COUNTER_Y = GAME_HEIGHT - 20
# The source of the ball image displayed during a game.
BALL_SOURCE = "ball.jpg"
# The source of the chance message displayed during a game.
CHANCEMESSAGE_TEXT = "CLICK FOR ANOTHER SHOT!!! GET IT?"
# The color utilized for certain messages during a game.
MESSAGE_LINECOLOR = colormodel.WHITE
# The source of the chance screen image displayed during a game.
CHANCESCREEN_SOURCE = "chance.png"
# The source of the lose message 1 displayed during a game.
LOSEMESSAGE1_TEXT = 'GAME OVER, \n YOU TURNED DOWN...'
# The source of the lose message 2 displayed during a game.
LOSEMESSAGE2_TEXT = 'CLICK TO TRY TO TURN UP AGAIN!!!'
# The color utilized for the lose messages during a game.
LOSEMESSAGE_LINECOLOR = colormodel.BLACK
# The source of the lose screen image displayed during a game.
LOSESCREEN_SOURCE = "lose.jpg"
# The source of the welcome message displayed during a game.
WELCOMEMESSAGE_TEXT = 'CLICK TO RAVE!!!'
# The source of the welcome screen image displayed during a game.
WELCOMESCREEN_SOURCE = "welcome.jpeg"
# The source of the win message 1 displayed during a game.
WINMESSAGE1_TEXT = 'YOU TURNED UP!!!'
# The source of the win message 2 displayed during a game.
WINMESSAGE2_TEXT = 'CLICK TO TURN UP AGAIN!!!'
# The source of the win screen image displayed during a game.
WINSCREEN_SOURCE = "win.jpg"


### USE COMMAND LINE ARGUMENTS TO CHANGE NUMBER OF BRICKS IN ROW"""

"""sys.argv is a list of the command line arguments when you run
python. These arguments are everything after the work python. So
if you start the game typing

    python breakout.py 3 4

Python puts ['breakout.py', '3', '4'] into sys.argv. Below, we 
take advantage of this fact to change the constants BRICKS_IN_ROW
and BRICK_ROWS."""

try:
   if (not sys.argv is None and len(sys.argv) == 3):
        bs_in_row  = int(sys.argv[1])
        brick_rows = int(sys.argv[2])
        if (bs_in_row > 0 and brick_rows > 0):
            # ALTER THE CONSTANTS
            BRICKS_IN_ROW  = bs_in_row
            BRICK_ROWS     = brick_rows
            BRICK_WIDTH    = GAME_WIDTH / BRICKS_IN_ROW - BRICK_SEP_H
except: # LEAVE THE CONSTANTS ALONE
    pass
