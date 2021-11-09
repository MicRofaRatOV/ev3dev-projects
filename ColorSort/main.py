#!/usr/bin/env pybricks-micropython

from pybricks            import ev3brick as brick
from pybricks.hubs       import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color, Stop

ev3 = EV3Brick()

# Notes
"""
S1 - цвет
A - направляющий
D - гусеничный
0,1,2 - позиции
"""

# VARS
Turn_Angle = 65
Turn_Speed = 150
Last_Pos = 1
Main_Speed = 200

# FNS
def turn(new, last):
    global Turn_Angle
    return (new - last)*Turn_Angle

def color_to_number(col):
    # Позиция красного - 0, зелёного - 1, жёлтого - 2
    # Число -1 означает другой цвет/его отсутствие
    if col == Color.RED:
        return 0
    elif  col == Color.GREEN:
        return 1
    elif  col == Color.YELLOW:
        return 2
    else:
        return -1

def main():
    global Last_Pos, Main_Speed
    t_motor = Motor(Port.A)
    t_motor.reset_angle(0)
    m_motor = Motor(Port.D)
    color_sensor = ColorSensor(Port.S1)
    # Запуск основной гусеницы
    m_motor.run(-Main_Speed)
    while True:
        color_now = color_to_number(color_sensor.color())
        if color_now != -1:
            t_motor.run_angle(Turn_Speed, turn(color_now, Last_Pos), then=Stop.HOLD, wait=True)
            Last_Pos = color_now



if __name__ == "__main__":
    main()