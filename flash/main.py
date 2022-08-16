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


setScreenColor(0x111111)

hat_dlight_0 = hat.get(hat.DLIGHT)
hat_dlight_0.set_mode(0x11)
lux = None
f_list = [2, 4, 8, 11]
iso = 400

lcd.orient(lcd.LANDSCAPE)
titleLux = M5TextBox(5, 5, "Lux:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueLux = M5TextBox(50, 5, "lux", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleEv = M5TextBox(100, 5, "EV:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueEv = M5TextBox(145, 5, "ev", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF2 = M5TextBox(5, 40, "F2:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF4 = M5TextBox(5, 60, "F4:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF8 = M5TextBox(5, 80, "F8:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF11 = M5TextBox(5, 100, "F11:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF2 = M5TextBox(50, 40, "f2", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF4 = M5TextBox(50, 60, "f4", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF8 = M5TextBox(50, 80, "f8", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF11 = M5TextBox(50, 100, "f11", lcd.FONT_DejaVu18, 0xffffff, rotate=0)


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
