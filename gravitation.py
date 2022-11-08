import math
import random
from tkinter import Tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from vect2d import Vect2D

class App(Tk):
    def __init__(self):
        super().__init__()
        self.__width = 800
        self.__height = 600

        self.title('Gravity Simulator')
        self.geometry(str(self.__width) + 'x' + str(self.__height))

        self.__world = World(self, self.__width, self.__height)
       
        self.bind('<space>', lambda _: self.__world.toggle())
        self.bind('<KeyPress>', self.__world.handle_arrow)
        self.bind('<KeyRelease>', self.__world.handle_arrow)
       
        # main loop for moving entities
        self.__world.ticker()
        

class World(ttk.Frame):

    def __init__(self, parent, width=50, height=50):
        super().__init__(parent)
        self.__width = width
        self.__height = height
        self.__entities = []
        self.__ticker_enabled = True
        self.__gravity_enabled = False
        self.__create_balls()
        self.__main_label = ttk.Label(self)
        self.__draw()
        self.__keys = [False, False, False, False]
        
        self.pack()
    
    def toggle(self):
        self.__ticker_enabled = not self.__ticker_enabled

    def toggle_gravity(self):
        self.__gravity_enabled = not self.__gravity_enabled

    def handle_arrow(self, event):
        if event.type == '2':     
            if event.keysym == 'g':
                self.__gravity_enabled = True
        elif event.type == '3':
            if event.keysym == 'g':
                self.__gravity_enabled = False
        #check if key is pressed or released    
        for entity in self.__entities:
            entity.__calc_velocity = Vect2D(0,0)

            if event.type == '2':
                if event.keysym == 'Left':
                    self.__keys[0] = True
                if event.keysym == 'Right':
                    self.__keys[1] = True
                if event.keysym == 'Up':
                    self.__keys[2] = True
                if event.keysym == 'Down':
                    self.__keys[3] = True
                    
                #calculate velocity
                if self.__keys[0]:
                    entity.__calc_velocity.x = -1
                if self.__keys[1]:
                    entity.__calc_velocity.x = 1
                if self.__keys[2]:
                    entity.__calc_velocity.y = -1
                if self.__keys[3]:
                    entity.__calc_velocity.y = 1
            elif event.type == '3':
                if event.keysym == 'Left':
                    self.__keys[0] = False
                    entity.__calc_velocity.x += 1
                if event.keysym == 'Right':
                    self.__keys[1] = False
                    entity.__calc_velocity.x -= 1
                if event.keysym == 'Up':
                    self.__keys[2] = False
                    entity.__calc_velocity.y += 1
                if event.keysym == 'Down':
                    self.__keys[3] = False
                    entity.__calc_velocity.y -= 1
                
            entity.acceleration = entity.__calc_velocity
    
    def __create_balls(self):
        for _ in range(30):
            random_ball_size = random.randint(10, 80)
            self.__entities.append(Ball(random_ball_size, Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)), Vect2D((random.randint(0, self.__width - random_ball_size)),(random.randint(0,self.__height - random_ball_size))), Vect2D((random.choice([-2,-1.5,-1, 1, 1.5, 2])),(random.choice([-2,-1.5,-1, 1, 1.5, 2]) )), Vect2D(0,0))) 
            
    def __draw(self):
        self.__background = Image.new(mode='RGB', size=(self.__width, self.__height), color=(0,0,0))
        draw = ImageDraw.Draw(self.__background)
        for ball in self.__entities:
            draw.ellipse([ball.position.x, ball.position.y, ball.position.x + ball.radius, ball.position.y + ball.radius], fill=(ball.color._r, ball.color._g, ball.color._b), width=0)
            #lolipop
            #draw.line([ball.position.x + ball.radius*2, ball.position.y + ball.radius*2, ball.position.x + ball.radius/2 + ball.acceleration.x * 10, ball.position.y + ball.radius/2 + ball.acceleration.y * 10], fill=(255,255,255), width=1)
            

        self.__image = ImageTk.PhotoImage(self.__background)  
        self.__main_label['image'] = self.__image 
        self.__main_label.pack()
        
        
    def ticker(self):
        if self.__ticker_enabled:
            for ball in self.__entities:
                ball.tick(Vect2D(self.__width, self.__height), self.__entities, self.__gravity_enabled)
            self.__draw()
        self.after(1, self.ticker)


class Entity():
    def __init__(self, position=(0,0), speed = (0,0), acceleration = (0,0)):
        self.__position = position
        self.__speed = speed
        self.__acceleration = acceleration
        
    @property
    def position(self):
        return self.__position
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def acceleration(self):
        return self.__acceleration
    
    @position.setter
    def position(self, value):
        self.__position = value
        
    @speed.setter
    def speed(self, value):
        self.__speed = value
        
    @acceleration.setter
    def acceleration(self, value):
        self.__acceleration = value
    
    def tick():
        pass


class Color():
    def __init__(self, r, g, b, a=255):
        self._r = r
        self._g = g
        self._b = b
        self._a = a


class Ball(Entity):
    def __init__(self, radius, color, position = (0,0), speed = (0,0), acceleration = (0,0)):
        super().__init__(position, speed, acceleration)
        self.__radius = radius
        self.__color = color
        self.__mass = ((4/3) * math.pi * (self.__radius ** 3))

    @property
    def radius(self):
        return self.__radius
    
    @property
    def color(self):
        return self.__color
    
    @property
    def mass(self):
        return self.__mass
    
    def tick(self, borders, entities, gravity_enabled):
        #handle gravity
        self.speed = Vect2D(self.speed.x + (self.acceleration.x), self.speed.y + (self.acceleration.y))
        self.position = Vect2D(self.position.x + self.speed.x, self.position.y + self.speed.y)
        # check for collisions
        if self.position.x + self.radius >= borders.x:
            self.position.x = borders.x - self.radius
            self.speed.x *= -0.85
            self.acceleration.x *= -1
            self.acceleration.y *= -1
        if self.position.x <= 0:
            self.position.x = 0
            self.speed.x *= -0.85
            self.acceleration.x *= -1
            self.acceleration.y *= -1
        if self.position.y + self.radius >= borders.y:
            self.position.y = borders.y - self.radius
            self.speed.y *= -0.85
            self.acceleration.x *= -1
            self.acceleration.y *= -1
        if self.position.y <= 0:
            self.position.y = 0
            self.speed.y *= -0.85
            self.acceleration.x *= -1
            self.acceleration.y *= -1
        
        if gravity_enabled:
            a = 1
            G = 0.0005
            acceleration = Vect2D()
            for i in entities:
            #calculate acceleration
                if self != i:
                    dist = self.position-i.position
                    acceleration += i.mass * dist/(dist.length_squared + a**2)**(3/2)
            acceleration *= G
            self.acceleration = acceleration


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()