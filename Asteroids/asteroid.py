import pyglet
import random
import math

window = pyglet.window.Window()

objects = []
ACCELERATION = 20   #pixels per seconds ^2
ROTATION_SPEED = 5      #spaceship, handle keys
MAX_ASTEROID_ROT_SPEED = 3
MAX_ASTEROID_SPEED = 30
MIN_LASER_SPEED = 20
pressed_keys = set()
batch = pyglet.graphics.Batch()

class SpaceObject:

    def __init__(self,  x=window.width//2,
                y=window.height//2,
                x_speed=0,
                y_speed=0,
                rot=0,
                image_index = 0         #starting index in list of images
                ):                      #using for choice of size of new Asteroids

        objects.append(self)
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rotation = rot
        self.image_index = image_index
        image = self.image_choice(image_index)
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
        self.sprite = pyglet.sprite.Sprite(image,batch=batch)
        radius = (image.width//2 + image.height//2)/2.2     #radius for collision
        self.radius = radius


    def update_position(self,t):
        """Obnovovani pozice a najeti do obrazku, pokud z nej objekt vyjede"""
        self.x += t* self.x_speed
        self.y += t* self.y_speed

        self.x %= window.width
        self.y %= window.height


    def update_sprite(self):

        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation  = 90 - math.degrees(self.rotation)

    def image_choice(self, image_index)  :
        """Choice of image"""
        raise NotImplementedError


    def delete(self):
        """Remove object """
        objects.remove(self)
        self.sprite.delete()


    def distance(self, a, b, wrap_size):            #a, b - objects
        """Distance in one direction (x or y)"""
        result = abs(a - b)
        if result > wrap_size / 2:
            result = wrap_size - result
        return result

    def overlaps(self, a, b):
        """Returns true iff two space objects overlap"""
        distance_squared = (self.distance(a.x, b.x, window.width) ** 2 +
                            self.distance(a.y, b.y, window.height) ** 2)
        max_distance_squared = (a.radius + b.radius) ** 2
        return distance_squared < max_distance_squared


    def hit_by_spaceship(self, ship):
        pass

    def hit_by_laser(self, asteroid):
        pass

    def tick(self, t):
        """Tika"""
        self.update_position(t)
        self.update_sprite()


class SpaceShip(SpaceObject):
    firing = -1             #setting the values for shooting,
                            #if firing < 0, SpaceShip can shoot
    def __init__(self,  x=window.width//2, y=window.height//2, x_speed=0, y_speed=0, rot=0):
        super().__init__()

    def handle_keys(self, t):

        if pyglet.window.key.UP in pressed_keys:
            self.x_speed += t * ACCELERATION * math.cos(self.rotation)
            self.y_speed += t * ACCELERATION * math.sin(self.rotation)

        if pyglet.window.key.LEFT in pressed_keys:
            self.rotation += ROTATION_SPEED * t

        if pyglet.window.key.RIGHT in pressed_keys:
            self.rotation -= ROTATION_SPEED * t

        if pyglet.window.key.SPACE in pressed_keys:

            if  self.firing < 0:                #firing of SpaceShip
                self.firing = 0.3
                laser = Laser(self.x,           #new laser
                              self.y,
                              self.x_speed,
                              self.y_speed,
                              self.rotation
                              )


    def image_choice(self, image_index):

        return pyglet.image.load(random.choice(['playerShip2_red.png',
                                                'playerShip3_green.png',
                                                'spaceship.png'])
                                                )

    def tick(self, t ):
        """Tika"""

        self.handle_keys (t)
        super().tick(t)
        self.firing = self.firing - t       #count down

        for obj in objects:                 #collision control
            if obj != self :
                if self.overlaps(self,obj):
                    obj.hit_by_spaceship(self)



class Asteroids(SpaceObject):

    def __init__(self,
                x=window.width,
                y=window.height,
                x_speed=30,
                y_speed=30,
                rot=0,
                generation = 0,
                image_index = 0
                ):
        super().__init__(image_index = image_index)
        self.generation = generation
        if generation == 0:     #original asteroids
            if random.randint(0,1) == 0:

                self.x = 0
                self.y = y//random.randint(1,4)
            else:
                self.x = x//random.randint(1,4)
                self.y = 0

            self.x_speed = random.randint(-MAX_ASTEROID_SPEED, MAX_ASTEROID_SPEED)
            self.y_speed = random.randint(-MAX_ASTEROID_SPEED, MAX_ASTEROID_SPEED)


        else:                   # new asteroids - after of hit of laser
            self.x = x
            self.y = y
            self.x_speed = x_speed + 30     #faster then original asteroids
            self.y_speed = y_speed + 30


        self.rotation_speed = random.randint(-MAX_ASTEROID_ROT_SPEED, MAX_ASTEROID_ROT_SPEED)    #



    def hit_by_spaceship(self, ship):  #removing the ship catching by asteroid
        """removing the ship"""
        ship.delete()

    def hit_by_laser( self, laser):
        """Removing of asteroids and the creation of two new smaller asteroids"""
        self.delete()                   # removing of asteroids catching by laser

        if laser in objects:
            laser.delete()
        if self.radius > 38:              #choose the right size of the new asteroids
           starting_position= 4           #(lower then original)
        elif self.radius > 18:
            starting_position= 6
        elif self.radius > 10:
           starting_position= 8

        else:
            return                        #'tiny' asteroid is destroyed after catching of laser
                
        for i in range(2):                #creation of two new asteroids with different of movement
            if i == 0:
                asteroid = Asteroids(x = self.x + 10,
                                    y = self.y + 10,
                                    x_speed = self.x_speed,
                                    y_speed = self.y_speed ,
                                    generation = 1,
                                    image_index = starting_position
                                    )
            else:

                asteroid = Asteroids(x = self.x - 10,
                                    y = self.y -10,
                                    x_speed=self.x_speed*(-1),
                                    y_speed=self.y_speed * (-1),
                                    generation = 1,
                                    image_index = starting_position
                                    )




    def tick(self, t):
        """Tika"""
        self.rotation += t*self.rotation_speed
        super().tick(t)

    def image_choice(self,image_index):
        print(image_index)                                                #list is sorted by size of radius
        list_of_asteroids = ['meteorGrey_big1.png',     # 0 - 3 big
                            'meteorGrey_big2.png',
                            'meteorGrey_big3.png',
                            'meteorGrey_big4.png',
                            'meteorGrey_med1.png',      # 4 - 5 med
                            'meteorGrey_med2.png',
                            'meteorGrey_small1.png',    # 6-7 small
                            'meteorGrey_small2.png',
                            'meteorGrey_tiny1.png',     # 8-9 tiny
                            'meteorGrey_tiny1.png'
                            ]


        return pyglet.image.load(random.choice(list_of_asteroids[self.image_index:]))


class Laser(SpaceObject):
    laser_live = 2              #settig the value for live time of laser

    def __init__(self,  x, y, x_speed=0, y_speed=0, rot=0):
        super().__init__()
        self.x = x
        self.y = y
        p = max(MIN_LASER_SPEED, math.sqrt(x_speed ** 2 + y_speed ** 2))
        self.x_speed = math.cos(rot) * (p+200)      #settig of speed of laser
        self.y_speed = math.sin(rot) * (p+200)      #faster then SpaceShip

        self.rotation = rot


    def hit_by_spaceship(self, ship):
        pass

    def image_choice(self, image_index):
        return pyglet.image.load(random.choice(['laserBlue01.png',
                                                'laserRed01.png'])
                                                )


    def tick(self, t ):
        """Tika"""
        super().tick(t)
        self.laser_live = self.laser_live - t   #removing of laser after the lapse of time
        if self.laser_live <0 :
            self.delete()

        for obj in objects:             #collision control
            if obj != self :
                if self.overlaps(self,obj):
                    obj.hit_by_laser(self)



# start of game
for i in range(6):           #number of original Asteroids
    asteroid = Asteroids()
spaceship = SpaceShip()



def on_draw():
    window.clear()
    batch.draw()


def tick(t):
    for obj in objects:
        obj.tick(t)


def on_key_press(sym, mod):
    pressed_keys.add(sym)

def on_key_release(sym, mod):
    pressed_keys.discard(sym)

def draw():
    window.clear()

    for x_offset in (-window.width, 0, window.width):
        for y_offset in (-window.height, 0, window.height):
            # Remember the current state
            gl.glPushMatrix()
            # Move everything drawn from now on by (x_offset, y_offset, 0)
            gl.glTranslatef(x_offset, y_offset, 0)

            # Draw
            batch.draw()

            # Restore remembered state (this cancels the glTranslatef)
            gl.glPopMatrix()



window.push_handlers(
        on_draw = on_draw,
        on_key_press = on_key_press,
        on_key_release = on_key_release
)

pyglet.clock.schedule_interval(tick,1/30)

pyglet.app.run()
