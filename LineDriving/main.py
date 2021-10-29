#!/usr/bin/env pybricks-micropython

from pybricks            import ev3brick as brick
from pybricks.hubs       import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port

ev3 = EV3Brick()

# Notes
"""
123
"""

# VARS
MIN_LIGHT = 12

# FNS
# Езда по перекрёстка
def goto_perek(speed=600, a=0.5, l=0.4, b=4, c=0.1, d=15, dif=0, perek=False):
    global MIN_LIGHT
    ml = Motor(Port.B)
    mr = Motor(Port.C)
    sl = ColorSensor(Port.S2)
    sr = ColorSensor(Port.S3)
    integral = 0
    last_error = 0
    while True:
        if perek and sl.reflection() <= MIN_LIGHT and sr.reflection() <= MIN_LIGHT:
            ml.brake()
            mr.brake()
            break
        ref = sl.reflection() - sr.reflection() + dif
        integral = integral*a + ref
        new_error = ref - last_error
        last_error = ref
        angle = ref*l + (b*ref)**3 + integral*c + new_error*d
        ml.run(speed+angle)
        mr.run(speed-angle)
    return True

if __name__ == "__main__":
    goto_perek(speed=400, a=0.8, l=1.7, b=0.003, c=0.25, d=17.5, dif=0)


