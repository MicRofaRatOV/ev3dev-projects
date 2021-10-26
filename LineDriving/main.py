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
def goto_perek(speed=600, a=0.5, b=4, c=0.1, d=15, dif=0):
    global MIN_LIGHT
    ml = Motor(Port.B)
    mr = Motor(Port.C)
    sl = ColorSensor(Port.S2)
    sr = ColorSensor(Port.S3)
    integral = 0
    last_error = 0
    while True:
        #if sl.reflection() <= MIN_LIGHT and sr.reflection() <= MIN_LIGHT:
        #    ml.hold()
        #    mr.hold()
        #    return True
        ref = sl.reflection() - sr.reflection() + dif
        integral = integral*a + ref
        new_error = ref - last_error
        last_error = ref
        angle = ref*b + integral*c + new_error*d
        ml.run(speed+angle)
        mr.run(speed-angle)

if __name__ == "__main__":
    goto_perek(speed=600, a=0.5, b=4, c=0.1, d=15, dif=0)


