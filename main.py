from numbers import Number
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat
import math


def convertLux2Ev(lux, iso=100):
    ev = math.log2(lux / 2.5)
    step = math.log2(iso / 100)
    return ev - step


setScreenColor(0xffffff)

hat_dlight_0 = hat.get(hat.DLIGHT)

incr = None
lux = None
color = None


title0 = M5Title(title="DLIGHT", x=43, fgcolor=0xFFFFFF, bgcolor=0xff0000)
label0 = M5TextBox(0, 38, "Lux:", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
# rectangle1 = M5Rect(0, 130, 135, 10, 0x000000, 0xFFFFFF)
# rectangle2 = M5Rect(0, 150, 135, 10, 0x000000, 0xFFFFFF)
# rectangle3 = M5Rect(0, 169, 135, 10, 0x000000, 0xFFFFFF)
# rectangle4 = M5Rect(0, 190, 135, 10, 0x000000, 0xFFFFFF)
# rectangle5 = M5Rect(0, 210, 135, 10, 0x000000, 0xFFFFFF)
# rectangle0 = M5Rect(0, 109, 135, 10, 0x000000, 0xFFFFFF)
# rectangle6 = M5Rect(0, 230, 135, 10, 0x000000, 0xFFFFFF)
label1 = M5TextBox(91, 70, "1", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
label2 = M5TextBox(45, 38, "label2", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
label3 = M5TextBox(0, 70, "Bit Shift:", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
label4 = M5TextBox(0, 90, "EV:", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
label5 = M5TextBox(45, 90, "label4:", lcd.FONT_DejaVu18, 0xff0000, rotate=0)


def buttonA_wasPressed():
    global incr, lux, color
    incr = (incr if isinstance(incr, Number) else 0) + 1
    if incr > 8:
        incr = 1
    label1.setText(str(incr))
    pass


btnA.wasPressed(buttonA_wasPressed)


incr = 1
hat_dlight_0.set_mode(0x11)
while True:
    lux = hat_dlight_0.get_lux()
    label2.setText(str(lux))
    label5.setText(str(convertLux2Ev(lux)))
    # color = lux >> incr
    # rectangle0.setBgColor((color << 16) | (color << 8) | color)
    # rectangle1.setBgColor((color << 16) | (0 << 8) | 0)
    # rectangle2.setBgColor((color << 16) | (color << 8) | 0)
    # rectangle3.setBgColor((0 << 16) | (color << 8) | 0)
    # rectangle4.setBgColor((0 << 16) | (color << 8) | color)
    # rectangle5.setBgColor((0 << 16) | (0 << 8) | color)
    # rectangle6.setBgColor((color << 16) | (0 << 8) | color)
    wait_ms(150)
    wait_ms(2)
