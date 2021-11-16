#!/usr/bin/env pybricks-micropython

from pybricks            import ev3brick as brick
from pybricks.hubs       import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port

ev3 = EV3Brick()

# Notes
"""
Right -  plus
Left - minus
"""

# VARS
SPEED = 100
ANGLE = -120

# FNS
def goto_angle(a):
    global SPEED
    ml = Motor(Port.B)
    mr = Motor(Port.C)
    gyro = GyroSensor(Port.S4)
    gyro.reset_angle(0)
    if a < 0:
        ml.run(SPEED)
        mr.run(-SPEED)
    elif a > 0:
        ml.run(-SPEED)
        mr.run(SPEED)
    else:
        return
    while abs(gyro.angle()) < abs(a):
        pass
    ml.brake()
    mr.brake()
    return

def main():
    global ANGLE
    goto_angle(ANGLE)

if __name__ == "__main__":
    main()