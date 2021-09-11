import pyglet


'''

Pong Window

Subclass of Pyglet Window that serves as the game

'''
class PongWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        #Call super to start up window setup
        super(PongWindow, self).__init__(*args, **kwargs)
    




    '''

    Basic window setup

    '''
    def initialize(self):
        return 


    '''

    Drawing method

    '''
    def on_draw(self):
        #Clear before drawing
        self.clear()
        #Draw




