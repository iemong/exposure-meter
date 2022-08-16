from numbers import Number
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat
import math


def convertLux2Ev(lux, iso=100):
    ev = round(math.log2(lux / 2.5))
    step = math.log2(iso / 100)
    return ev - step


def calcSS(ev):
    return lambda av: math.floor(1 / (2 ** (-1 * (ev - 2 * math.log2(av)))))


setScreenColor(0xffffff)

hat_dlight_0 = hat.get(hat.DLIGHT)
hat_dlight_0.set_mode(0x11)
lux = None
f_list = [2, 4, 8, 11]
iso = 400

lcd.orient(lcd.LANDSCAPE)
titleLux = M5TextBox(0, 38, "Lux:", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
valueLux = M5TextBox(45, 38, "lux", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
titleEv = M5TextBox(0, 90, "EV:", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
valueEv = M5TextBox(45, 90, "ev", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
titleF2 = M5TextBox(0, 120, "F2:", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
titleF4 = M5TextBox(0, 140, "F4:", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
titleF8 = M5TextBox(0, 160, "F8:", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
titleF11 = M5TextBox(0, 180, "F11:", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
valueF2 = M5TextBox(45, 120, "f2", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
valueF4 = M5TextBox(45, 140, "f4", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
valueF8 = M5TextBox(45, 160, "f8", lcd.FONT_DejaVu18, 0xff0000, rotate=0)
valueF11 = M5TextBox(45, 180, "f11", lcd.FONT_DejaVu18, 0xff0000, rotate=0)


while True:
    lux = hat_dlight_0.get_lux()
    ev = convertLux2Ev(lux, iso)
    tv_list = list(map(calcSS(ev), f_list))
    valueLux.setText(str(lux))
    valueEv.setText(str(ev))
    valueF2.setText(str(tv_list[0]))
    valueF4.setText(str(tv_list[1]))
    valueF8.setText(str(tv_list[2]))
    valueF11.setText(str(tv_list[3]))
    wait_ms(150)
