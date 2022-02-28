from __future__ import annotations

class Vector(object):
    _x: int | float
    _y: int | float
    _z: int | float


    def __init__(self, x: int | float, y: int | float, z: int | float):
        self._x = x
        self._y = y
        self._z = z


    @property
    def x(self) -> int:
        return self._x


    @property
    def y(self) -> int:
        return self._y


    @property
    def z(self) -> int:
        return self._z


    def __eq__(self, other: Vector) -> bool:
        return self._x == other._x and self._y == other._y and self._z == other._z


    def __add__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self._x + other._x, self._y + other._y, self._z + other._z)
        
        if isinstance(other, (int, float)):
            return Vector(self._x + other, self._y + other, self._z + other)


    def __sub__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self._x - other._x, self._y - other._y, self._z - other._z)
        
        if isinstance(other, (int, float)):
            return Vector(self._x - other, self._y - other, self._z - other)

    def __mul__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self._y * other._z - self._z * other._y,
                self._z * other._x - self._x * other._z,
                self._x * other._y - self._y * other._x
            )
    
        if isinstance(other, (int, float)):
            return Vector(self._x * other, self._y * other, self._z * other)

    def __mod__(self, other: int | float) -> Vector | int:
        if isinstance(other, Vector):
            return self._x * other._x + self._y * other._y + self._z * other._z
    
        if isinstance(other, (int, float)):
            return Vector(self._x % other, self._y % other, self._z % other)
    
