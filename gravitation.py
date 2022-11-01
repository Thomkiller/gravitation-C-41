import random
from tkinter import Tk
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Gravity Simulator')

        test = World(self)
    

class World(ttk.Frame):

    def __init__(self, parent, width=50, height=50):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.entities = []
        self.create_balls 
        print('after')

    def create_balls(self):
        for i in range(20):
            self.entities.append(Ball(random.randint(1,10), Color(random.randint(0,255),random.randint(0,255),random.randint(0,255),255)))

    

        

class Entity():
    def __init__(self, position, speed, acceleration):
        self._position = position
        self._speed = speed
        self._acceleration = acceleration
    
    def tick():
        pass

class Color():
    def __init__(self, r, g, b, a):
        self._r = r
        self._g = g
        self._b = b
        self._a = a

class Ball(Entity):
    def __init__(self, radius, color):
        super().__init__()


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()