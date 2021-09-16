#!/usr/bin/env pybricks-micropython

from pybricks            import ev3brick as brick
from pybricks.hubs       import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, TouchSensor
from pybricks.parameters import Port

ev3 = EV3Brick()

# Notes
"""
264 - максимальный угол башни
"""

# VARS
SPEED_RADAR = 50
SPEED_GUN = 800
DISTANCE = 300
angle = 0

# FNS
def posr():
    global SPEED_RADAR
    motor =  Motor(Port.D)
    sensor = TouchSensor(Port.S1)
    motor.run(SPEED_RADAR)
    while True:
        if sensor.pressed():
            motor.hold()
            break

def fpos():
    global SPEED_RADAR, DISTANCE
    end_once = False
    motor =  Motor(Port.D)
    sensor =  UltrasonicSensor(Port.S4)
    a = 0
    motor.run(-SPEED_RADAR)
    while True:
        if motor.angle() <= -264: 
            motor.run(SPEED_RADAR)
            end_once = True
        elif motor.angle() >= 0 and end_once:
            motor.run(-SPEED_RADAR)
        elif sensor.distance() <= DISTANCE:
            a = motor.angle()
            motor.stop()
            break
    return a

def strike():
    global SPEED_GUN
    motor =  Motor(Port.A)
    motor.run(250)
    while True:
        if motor.angle() >= 360:
            motor.hold()
            break

def gpos(a):
    global SPEED_RADAR
    motor =  Motor(Port.C)
    motor.run_angle(SPEED_RADAR, -a)
    strike()
    motor.run_angle(SPEED_RADAR, a)


if __name__ == "__main__":
    for i in range(5):
        posr()
        angle = fpos()
        gpos(angle)

