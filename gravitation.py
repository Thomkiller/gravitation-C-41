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

        test = World(self, self.__width, self.__height)


class World(ttk.Frame):

    def __init__(self, parent, width=50, height=50):
        super().__init__(parent)
        self.__width = width
        self.__height = height
        self.__entities = []
        self.__create_balls()
        self.__main_label = ttk.Label(self)
        self.__draw()
        self.pack()
    
    def __create_balls(self):
        for _ in range(20):
            self.__entities.append(Ball(random.randint(1,100), Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))) 
            
    def __draw(self):
        self.__background = Image.new(mode='RGB', size=(self.__width, self.__height), color=(0,0,0))
        draw = ImageDraw.Draw(self.__background)
        for ball in self.__entities:
            draw.ellipse([ball.position[0], ball.position[1], ball.position[0] + ball.radius, ball.position[1] + ball.radius], fill=(ball.color._r, ball.color._g, ball.color._b), width=0)
        self.__image = ImageTk.PhotoImage(self.__background)  
        self.__main_label['image'] = self.__image 
        self.__main_label.pack()

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
    
    def tick():
        pass


class Color():
    def __init__(self, r, g, b, a=255):
        self._r = r
        self._g = g
        self._b = b
        self._a = a


class Ball(Entity):
    def __init__(self, radius, color):
        super().__init__()
        self.__radius = radius
        self.__color = color

    @property
    def radius(self):
        return self.__radius
    
    @property
    def color(self):
        return self.__color


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()