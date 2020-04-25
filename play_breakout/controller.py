# controller.py
# Allie Meng (awm79) and Mary Gibbs (meg297)
# 5/6/14


"""Primary module for Breakout application. This module contains the controller
class for the Breakout application. There should not be any need for additional
classes in this module. If you need more classes, 99% of the time they belong
in the model module. If you are unsure about where a new class should go, post a
question on Piazza."""


from constants import *
from game2d import *
from model import *


sound = Sound('sound.wav')
sound.play()


class Breakout(Game):
    """Instance is a Breakout application. This class extends Game and
    implements the various methods necessary for running the game. Method init
    starts up the game. Method update updates the model objects (e.g. move ball,
    remove self.lives = 3). Method draw displays all of the models on the
    screen. Most of the work handling the game is actually provided in the class
    Model. Model should have a method called moveBall() that moves the ball, and
    processes all of the game physics. This class should simply call that method
    in update(). The primary purpose of this class is managing the game state:
    when is the game started, paused, completed, etc. It keeps track of that in
    an attribute called state.

    Instance Attributes:

        bricksmessage: The message displayed after a brick is destroyed during
        a game. [None].  

        bricksmessagetime: The time for a bricksmessage during a game. [int].

        chancemessage: The chance message displayed after the ball disappears
        after it collides with the bottom of the screen during a game. [GLabel].
        
        chancescreen: The chance screen image displayed after the ball
        disappears after it collides with the bottom of the screen during a
        game. [GImage].

        losemessage1: The lose message displayed after the number of lives drops
        to zero during a game. [GLabel].

        losemessage2: The lose message displayed after the number of lives drops
        to zero during a game. [GLabel].

        losescreen: The lose screen image displayed after the number of lives
        drops to zero during a game. [GImage].

        model: The game model, which stored the paddle, ball, and bricks.
        [GModel, or None if there is no game currently active. It is only
        None if state is STATE_INACTIVE].

        previoustouch: Stores the touch attribute of GView in the previous
        update() call to keep track of the state of the mouse. [Either a GPoint
        object or None].

        state: The current state of the game. [One of STATE_INACTIVE,
        STATE_COUNTDOWN, STATE_PAUSED, STATE_ACTIVE, STATE_COMPLETE, or
        STATE_STARTAGAIN].

        time: Keeps track of how much time has passed since the start of the
        game. [float].

        view: The game view, used in drawing. [Immutable instance of GView. It
        is inherited from Game].

        welcomemessage: The welcome message displayed during the beginning of
        the game. [GLabel].

        welcomescreen: The welcome screen image displayed during the beginning
        of the game. [GImage].

        winmessage1: The win message displayed after all of the bricks have
        been destroyed during a game. [GLabel].

        winmessage2: The win message displayed after all of the bricks have
        been destroyed during a game. [GLabel].
        
        winscreen: The win screen image displayed after all of the bricks have
        been destroyed during a game. [GImage]."""

    def init(self):
	    """Initialize the game state. This method is distinct from the built-in
        initializer __init__. This method is called once the game is running.
        You should use it to initialize any game specific attributes. This
        method should initialize any state attributes as necessary to satisfy
        invariants. When done, set the state to STATE_INACTIVE, and create a
        message saying that the user should press to play a game."""
        self.bricksmessage = None

        self.bricksmessagetime = 0

        self.chancemessage = GLabel(text = CHANCEMESSAGE_TEXT, font_name = FONT,
        font_size = 20, linecolor = MESSAGE_LINECOLOR, x = GAME_WIDTH/2.0,
        y = 60, halign = 'center', valign = 'middle')

        self.chancescreen = GImage(source = CHANCESCREEN_SOURCE,
        width = GAME_WIDTH, height = GAME_HEIGHT, center_x = GAME_WIDTH/2.0,
        center_y = GAME_HEIGHT/2)

        self.losemessage1 = GLabel(text = LOSEMESSAGE1_TEXT, font_name = FONT,
        font_size = 40, linecolor = LOSEMESSAGE_LINECOLOR, x = GAME_WIDTH/2,
        y = GAME_HEIGHT*(3.0/4.0), halign = 'center', valign = 'middle')

        self.losemessage2 = GLabel(text = LOSEMESSAGE2_TEXT, font_name = FONT,
        font_size = 20, linecolor = LOSEMESSAGE_LINECOLOR, x = GAME_WIDTH/2,
        y = GAME_HEIGHT*(3.0/4.0) - 80, halign = 'center', valign = 'middle')

        self.losescreen = GImage(source = LOSESCREEN_SOURCE, width = 300,
        height = 300, center_x = GAME_WIDTH/2, center_y = GAME_HEIGHT*(1.0/4.0))

        self.model = None

        self.previoustouch = None

        self.state = STATE_INACTIVE

        self.time = 0

        self.welcomemessage = GLabel(text = WELCOMEMESSAGE_TEXT,
        font_name = FONT, font_size = 45, linecolor = MESSAGE_LINECOLOR, 
        x = GAME_WIDTH/2, y = GAME_HEIGHT*(5.0/6.0), halign = 'center',
        valign = 'middle')

        self.welcomescreen = GImage(source = WELCOMESCREEN_SOURCE,
        width = GAME_WIDTH, height = GAME_HEIGHT, center_x = GAME_WIDTH/2,
        center_y = GAME_HEIGHT/2)

        self.winmessage1 = GLabel(text = WINMESSAGE1_TEXT, font_name = FONT,
        font_size = 45, linecolor = MESSAGE_LINECOLOR, x = GAME_WIDTH/2,
        y= GAME_HEIGHT*(3.0/4.0), halign = 'center', valign = 'middle')

        self.winmessage2 = GLabel(text = WINMESSAGE2_TEXT, font_name = FONT,
        font_size = 20, linecolor = MESSAGE_LINECOLOR, x = GAME_WIDTH/2,
        y = GAME_HEIGHT*(3.0/4.0) - 60, halign = 'center', valign = 'middle')

        self.winscreen = GImage(source = WINSCREEN_SOURCE, width = GAME_WIDTH,
        height = GAME_HEIGHT, center_x = GAME_WIDTH/2, center_y = GAME_HEIGHT/2)


    def update(self,dt):
	    """Animate a single frame in the game. It is the method that does most
        of the work. Of course, it should rely on helper methods in order to
        keep the method short and easy to read. Some of the helper methods
        belong in this class, and others belong in class Model. The first thing
        this method should do is to check the state of the game. One thing that
        you can do here to organize your code is to have a helper method for
        each of your states, as the game must do different things in each state.

        In STATE_INACTIVE, the method checks to see if the player clicks
        the mouse. If so, it starts a new game and switches to STATE_COUNTDOWN.

        STATE_PAUSED is similar to STATE_INACTIVE. However, instead of 
        starting a whole new game, it simply switches to STATE_COUNTDOWN.

        In STATE_COUNTDOWN, the game counts down until the ball is served.
        The player is allowed to move the paddle, but there is no ball.
        This state should delay three seconds.

        In STATE_ACTIVE, the game plays normally. The player can move the
        paddle and the ball moves on its own about the board.

        While in STATE_ACTIVE, if the ball goes off the screen and there
        are lives left, it switches to STATE_PAUSED. If the ball is lost 
        with no lives left, the game is over and it switches to
        STATE_COMPLETE. It should also switch to STATE_COMPLETE once there
        are no bricks left, since that means the player has won.

        While in STATE_COMPLETE, this method does nothing.

        You are allowed to add more states if you wish. Should you do so,
        you must describe them here.

        Precondition: dt is the time since last update (a float). This
        parameter can be safely ignored most of the time. It is only
        relevant for debugging if your game is running really slowly."""
        if self.state == STATE_INACTIVE and self.view.touch != None:
            newmodel = Model()
            self.model = newmodel
            self.state = STATE_COUNTDOWN

        if self.state == STATE_COUNTDOWN or self.state == STATE_ACTIVE:
            self.movepaddle()
          
        if self.state == STATE_COUNTDOWN and self.time >= 3:
            self.state = STATE_ACTIVE

        if self.state == STATE_PAUSED and self.previoustouch == None\
        and self.view.touch != None:
            self.time = 0
            self.state = STATE_COUNTDOWN
        
        self.dt = dt
        if self.state == STATE_COUNTDOWN:
            self.model.createball()
            self.time += dt
        
        if self.state == STATE_PAUSED:
            self.previoustouch = self.view.touch
        
        if self.state == STATE_ACTIVE and self.model.lives > 0\
        and self.model.loseball():
            self.state = STATE_PAUSED
            
        if (self.state == STATE_ACTIVE and len(self.model.bricks) == 0)\
        or (self.state == STATE_PAUSED and self.model.lives == 0):
            self.state = STATE_COMPLETE
            
        if self.state == STATE_ACTIVE:
            self.model.ball.moveball()
            self.model.collisionconsequnce()

        if self.state == STATE_COMPLETE and self.previoustouch == None\
        and self.view.touch != None:
            self.state = STATE_INACTIVE
            self.time = 0

        if self.state == STATE_COMPLETE:
            self.previoustouch = self.view.touch


    def draw(self):
	    """Draws the game objects to the view. Every single thing you want to
        draw in this game is a GObject. To draw a GObject g, simply use the
        method g.draw(view). It is that easy! Many of the GObjects, such as the
        paddle, ball, and bricks, are attributes in Model. In order to draw
        them, you either need to add getters for these attributes or you need to
        add a draw method to class Model. Which one you do is up to you."""
        if self.state == STATE_INACTIVE:
            self.welcomescreen.draw(self.view)
            self.welcomemessage.draw(self.view)

        if self.state == STATE_COUNTDOWN or self.state == STATE_ACTIVE:
            self.model.background.draw(self.view)
            self.model.paddle.draw(self.view)
            for brick in self.model.bricks:
                brick.draw(self.view)
            self.model.ball.draw(self.view)
            self.model.livescounter.draw(self.view)
            self.model.scorecounter.draw(self.view)

        if self.state == STATE_ACTIVE and self.bricksmessage\
        != self.model.bricksmessage:
            self.bricksmessagetime = 0

        if  self.state == STATE_ACTIVE and self.model.bricksmessage != None\
        and self.bricksmessagetime <= 0.5:
            self.bricksmessagetime += self.dt
            self.model.bricksmessage.draw(self.view)

        if self.state == STATE_PAUSED and self.model.lives > 0:
            self.chancescreen.draw(self.view)
            self.chancemessage.draw(self.view)

        if self.state == STATE_COMPLETE and self.model.lives == 0:
            self.losescreen.draw(self.view)
            self.losemessage1.draw(self.view)
            self.losemessage2.draw(self.view)

        if self.state == STATE_COMPLETE and self.model.lives != 0:
            self.winscreen.draw(self.view)
            self.winmessage1.draw(self.view)
            self.winmessage2.draw(self.view)

        if self.state == STATE_ACTIVE:
            self.bricksmessage = self.model.bricksmessage


    def movepaddle(self):
	    """Moves the paddle."""
        if self.previoustouch == None and self.view.touch != None:
            self.previoustouch = self.view.touch
            return

        if self.previoustouch !=None and self.view.touch != None:
            distance = self.view.touch.x - self.previoustouch.x
            self.model.paddle.center_x += distance
            self.previoustouch = self.view.touch

        if self.view.touch == None and self.previoustouch != None:
           self.previoustouch = None
           return

        if self.model.paddle.x < 0:
            self.model.paddle.x = 0
        
	    if self.model.paddle.x + PADDLE_WIDTH > GAME_WIDTH:
            self.model.paddle.x = GAME_WIDTH - PADDLE_WIDTH
