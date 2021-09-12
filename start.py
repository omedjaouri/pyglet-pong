#Pyglet import
import pyglet
import pyglet.gl as gl
#Local game import
from app.window import PongWindow


#Basic start
if __name__ == "__main__":
    #Set up the pyglet resource path
    pyglet.resource.path = ["./resources/"]
    pyglet.resource.reindex()
    #Create config for window
    config = gl.Config(double_buffer=True)
    #Create game window
    window = PongWindow(width=1200, height=800, caption='PONG', config=config)
    #Run the pyglet application (aka game)
    pyglet.app.run()

