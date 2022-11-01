from turtle import position, speed


class World():

    def __init__(self, width=50, height=50, entities=None):
        self.width = width
        self.height = height
        self.entities = entities

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


def main():
    pass

if __name__ == '__main__':
    main()