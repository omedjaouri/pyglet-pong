#Pyglet import
import pyglet
import pyglet.gl as gl
#Local game import
from app.window import PongWindow


#Basic start
if __name__ == "__main__":
    #Create config for window
    config = gl.Config(double_buffer=True)
    #Create game window
    window = PongWindow(width=800, height=600, caption='PONG', config=config)
    #Run the pyglet application (aka game)
    pyglet.app.run()

