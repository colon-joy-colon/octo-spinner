from typing import Tuple
from math import sin, cos, pi

Undefined = object()

class Value:
    def __init__(self, initial:object=None) -> None:
        self._value = initial

    def _call0(self, _v=Undefined):
        if _v is Undefined:
            return self._value
        else:
            previous = self._value

            self._value = _v

            return previous

    def __call__(self, _v=Undefined):
        return self._call0(_v)

def get_position(radius:float, percent:float) -> Tuple[float, float]:
    rad = percent*2*pi

    # (x, y)
    return (
        radius*cos(rad),
        radius*sin(rad)
    )
