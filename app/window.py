#Lib imports
import pyglet
import pyglet.window.key as key
#Local imports
from .player import *

'''

Pong Window

Subclass of Pyglet Window that serves as the game

'''
class PongWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        #Call super to start up window setup
        super(PongWindow, self).__init__(*args, **kwargs)
   
        #Create batch for batch drawing the sprites
        self.batch = pyglet.graphics.Batch()

        #Use the window size to determine where the player needs to be placed.
        player_init_pos = (100, self.height//2)

        #Instantiate a player
        self.player = Player(pos=player_init_pos, screen_height=self.height, batch=self.batch)

        #Create keystate handler
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        #Start clock-based callback
        pyglet.clock.schedule_interval(self.update, 1/60)

    '''

    Drawing method

    '''
    def on_draw(self):
        #Clear before drawing
        self.clear()

        #Draw the batches
        self.batch.draw()

    '''

    Periodic update function (60 fps)

    '''
    def update(self, dt):
        #Check for quit
        if self.keys[key.Q] or self.keys[key.ESCAPE]:
            self.close()

        #Update the player position
        self.player.update(self.keys, dt)



        return
