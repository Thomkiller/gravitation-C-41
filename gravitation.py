import random
from tkinter import Tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import vect2d

class App(Tk):
    def __init__(self):
        super().__init__()
        self.__width = 800
        self.__height = 600

        self.title('Gravity Simulator')
        self.geometry(str(self.__width) + 'x' + str(self.__height))

        self.__world = World(self, self.__width, self.__height)
       
        self.bind('<space>', lambda _: self.__world.toggle())
        self.bind('<Left>', lambda _: self.__world.key_left())
        self.bind('<Right>', lambda _: self.__world.key_right())
        self.bind('<Up>', lambda _: self.__world.key_up())
        self.bind('<Down>', lambda _: self.__world.key_down())
       
        # main loop for moving entities
        self.__world.ticker()
        

class World(ttk.Frame):

    def __init__(self, parent, width=50, height=50):
        super().__init__(parent)
        self.__width = width
        self.__height = height
        self.__entities = []
        self.__ticker_enabled = True
        self.__create_balls()
        self.__main_label = ttk.Label(self)
        self.__draw()
        
        self.pack()
    
    def toggle(self):
        self.__ticker_enabled = not self.__ticker_enabled
    
    def key_up(self):
        for entity in self.__entities:
            entity.acceleration = Point(0, -5)

    def key_down(self):
        for entity in self.__entities:
            entity.acceleration = Point(0, 5)

    def key_left(self):
        for entity in self.__entities:
            entity.acceleration = Point(-5, 0)
    
    def key_right(self):
        for entity in self.__entities:
            entity.acceleration = Point(5, 0)
    
    def __create_balls(self):
        for _ in range(20):
            random_ball_size = random.randint(10, 80)
            self.__entities.append(Ball(random_ball_size, Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)), Point((random.randint(0, self.__width - random_ball_size)),(random.randint(0,self.__height - random_ball_size))), Point((random.choice([-2,-1.5,-1, 1, 1.5, 2])),(random.choice([-2,-1.5,-1, 1, 1.5, 2]) )), Point(1,1))) 
            
    def __draw(self):
        self.__background = Image.new(mode='RGB', size=(self.__width, self.__height), color=(0,0,0))
        draw = ImageDraw.Draw(self.__background)
        for ball in self.__entities:
            draw.ellipse([ball.position.x, ball.position.y, ball.position.x + ball.radius, ball.position.y + ball.radius], fill=(ball.color._r, ball.color._g, ball.color._b), width=0)
        self.__image = ImageTk.PhotoImage(self.__background)  
        self.__main_label['image'] = self.__image 
        self.__main_label.pack()
        
    def ticker(self):
        if self.__ticker_enabled:
            for ball in self.__entities:
                ball.tick(Point(self.__width, self.__height))
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

    @property
    def radius(self):
        return self.__radius
    
    @property
    def color(self):
        return self.__color
    
    def tick(self, borders):
        # use vect2d to calculate new position
        self.position.x += self.speed.x
        self.position.y += self.speed.y
        # check for collisions
        if self.position.x + self.radius >= borders.x:
            self.position.x = borders.x - self.radius
            self.speed.x *= -1
            self.acceleration.x *= -1
            self.acceleration.y *= -1
        if self.position.x <= 0:
            self.position.x = 0
            self.speed.x *= -1
            self.acceleration.x *= -1
            self.acceleration.y *= -1
        if self.position.y + self.radius >= borders.y:
            self.position.y = borders.y - self.radius
            self.speed.y *= -1
            self.acceleration.x *= -1
            self.acceleration.y *= -1
        if self.position.y <= 0:
            self.position.y = 0
            self.speed.y *= -1
            self.acceleration.x *= -1
            self.acceleration.y *= -1
        

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()