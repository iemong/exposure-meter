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
f_list = [2, 2.8, 4, 5.6, 8, 11, 16]
iso = 400
iso_list = list([100, 200, 400, 800])

lcd.orient(lcd.LANDSCAPE)
# titleLux = M5TextBox(5, 5, "Lux:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
# valueLux = M5TextBox(50, 5, "lux", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleEv = M5TextBox(5, 5, "EV:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueEv = M5TextBox(45, 5, "ev", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleIso = M5TextBox(100, 5, "ISO:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueIso = M5TextBox(150, 5, "iso", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF2 = M5TextBox(5, 40, "F2:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF2_8 = M5TextBox(5, 60, "F2.8:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF4 = M5TextBox(5, 80, "F4:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF5_6 = M5TextBox(5, 100, "F5.6:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF8 = M5TextBox(130, 40, "F8:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF11 = M5TextBox(130, 60, "F11:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
titleF16 = M5TextBox(130, 80, "F16:", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF2 = M5TextBox(60, 40, "f2", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF2_8 = M5TextBox(60, 60, "f2.8", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF4 = M5TextBox(60, 80, "f4", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF5_6 = M5TextBox(60, 100, "f5.6", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF8 = M5TextBox(185, 40, "f8", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF11 = M5TextBox(185, 60, "f11", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
valueF16 = M5TextBox(185, 80, "f16", lcd.FONT_DejaVu18, 0xffffff, rotate=0)


def buttonA_wasPressed():
    global iso
    i = iso_list.index(iso)
    next_i = (i + 1) % 4
    iso = iso_list[next_i]


btnA.wasPressed(buttonA_wasPressed)


while True:
    lux = hat_dlight_0.get_lux()
    ev = convertLux2Ev(lux, iso)
    tv_list = list(map(calcSS(ev), f_list))
    # valueLux.setText(str(lux))
    valueEv.setText(str(ev))
    valueIso.setText(str(iso))
    valueF2.setText(str(tv_list[0]))
    valueF2_8.setText(str(tv_list[1]))
    valueF4.setText(str(tv_list[2]))
    valueF5_6.setText(str(tv_list[3]))
    valueF8.setText(str(tv_list[4]))
    valueF11.setText(str(tv_list[5]))
    valueF16.setText(str(tv_list[6]))
    wait_ms(150)
