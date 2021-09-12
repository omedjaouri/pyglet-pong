#Lib import
import pyglet
import pyglet.window.key as key
#Local imports


'''

Player Class


'''
class Player:
    #Initialize the player
    def __init__(self, pos=(0,0), screen_height=800, batch=None, speed=1000):
        #Set up member vars
        self.speed = speed
        self.x = pos[0]
        self.y = pos[1]
        self.screen_height=screen_height

        #Load the sprite for the player (setting up the batch)
        img = pyglet.resource.image('paddle.png')
        img.anchor_x = img.width // 2
        img.anchor_y = img.height // 2
        self.sprite = pyglet.sprite.Sprite(img, 
                                           x=pos[0], 
                                           y=pos[1], 
                                           batch=batch)
        #Update the sprite to scale it
        self.sprite.update(scale=2.0)


    '''
    
    Basic draw method

    '''
    def draw(self):
        #Draw the sprite for the player
        self.sprite.draw()

    '''

    Update the player based on user input

    '''
    def update(self, keys, dt):
        dy = 0
        #Check for movement direction
        if keys[key.W] or keys[key.UP]:
            dy = self.speed
        elif keys[key.S] or keys[key.DOWN]:
            dy = -self.speed

        #Calculate new position
        y = self.y + dy * dt
        #Clamp to the screen
        self.y = min(max(self.sprite.height // 2, y), 
                     self.screen_height - self.sprite.height // 2) 
        #Update sprite position
        self.sprite.update(y=self.y)
    
        return
