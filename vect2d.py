from math import sqrt, pi, tau, sin, cos, atan2, isclose
from random import uniform

class Vect2D:
    
    @classmethod
    def from_polar(cls, length : float, orientation : float) -> 'Vect2D':
        return cls(cos(orientation) * length, sin(orientation) * length)
    
    def __init__(self, x : int | float = 0., y : int | float = 0.) -> None:
        self.x = float(x)
        self.y = float(y)

    def set_polar(self, length : float, orientation : float) -> None:
        self.x = cos(orientation) * length
        self.y = sin(orientation) * length
        
    @property
    def is_defined(self) -> bool:
        return self.x != 0. or self.y != 0.
    
    @property
    def is_normalized(self) -> bool:
        return isclose(self.length_squared(), 1.0)
    
    @property
    def length_squared(self) -> float:
        return self.x ** 2. + self.y ** 2.

    @property
    def length(self) -> float:
        return sqrt(self.length_squared)
    
    @property
    def orientation(self) -> float:
        return atan2(self.y, self.x)

    def normalize(self) -> float:
        if self.is_defined:
            norm = self.length
            self.x /= norm
            self.y /= norm

    @property
    def normalized(self) -> 'Vect2D':
        vect = Vect2D(self.x, self.y)
        vect.normalize()
        return vect
    
    def reset(self) -> None:
        self.x = 0.
        self.y = 0.

    def randomize_normalized(self) -> None:
        self.set_polar(1.0, uniform(0., tau))

    def randomize_cartesian(self, minX, maxX, minY, maxY) -> None:
        self.x = uniform(minX, maxX)
        self.y = uniform(minY, maxY)

    # def randomize_polar(self, minLength, maxLength, minOrientation=0., maxOrientation=tau) -> None:
    #     self.set_polar(uniform(minLength, maxLength), uniform(minOrientation, maxOrientation))
    def randomize_polar(self, minLength, maxLength, rangeOrientation=tau, offsetOrientation=0.) -> None:
        self.set_polar(uniform(minLength, maxLength), uniform(0., rangeOrientation) + offsetOrientation)
        
    def __repr__(self) -> str:
        return f'vect2d.Vect2D(x={self.x}, y={self.y})'
        
    def __name__(self) -> str:
        return f'({self.x:0.2f}, {self.y:0.2f})'
    
    def __eq__(self, other : 'Vect2D') -> bool:
        return isclose(self.x, other.x) and isclose(self.y, other.y)
        
    def __add__(self, other : 'Vect2D') -> 'Vect2D':
        return Vect2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other : 'Vect2D') -> 'Vect2D':
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other : 'Vect2D') -> 'Vect2D':
        return Vect2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other : 'Vect2D') -> 'Vect2D':
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other : float) -> 'Vect2D':
        return Vect2D(self.x * other, self.y * other)

    def __rmul__(self, other : float) -> 'Vect2D':
        return Vect2D(self.x * other, self.y * other)

    def __imul__(self, other : float) -> 'Vect2D':
        self.x *= other
        self.y *= other
        return self

    def __truediv__(self, other : float) -> 'Vect2D':
        return Vect2D(self.x / other, self.y / other)

    def __rtruediv__(self, other: float) -> 'Vect2D':
        return Vect2D(other / self.x, other / self.y)

    def __itruediv__(self, other : float) -> 'Vect2D':
        self.x /= other
        self.y /= other
        return self
