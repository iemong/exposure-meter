import math
from numbers import Number
from m5stack import *
from m5ui import *
from uiflow import *
import time
import hat

def convert_lux_to_ev(lux, iso=100):
    if lux == 0:
        return 0
    ev = round(math.log2(lux / 2.5))
    step = math.log2(iso / 100)
    return ev + step

def calc_ss(ev):
    return lambda av: math.floor(1 / (2 ** (-1 * (ev - 2 * math.log2(av)))))

def update_tv_list(ev):
    return list(map(calc_ss(ev), f_list))

def update_ev():
    lux = hat_dlight_0.get_lux()
    ev = convert_lux_to_ev(lux, iso)
    tv_list = update_tv_list(ev)
    ui_elements["valueEv"].setText(str(ev))
    ui_elements["valueIso"].setText(str(iso))
    
    for idx, f_value in enumerate(f_list):
        ui_elements["valueF" + str(f_value)].setText(str(tv_list[idx]))

def buttonA_wasPressed():
    global iso
    i = iso_list.index(iso)
    next_i = (i + 1) % 4
    iso = iso_list[next_i]
    update_ev()

def buttonB_wasPressed():
    update_ev()

# Setup M5Stack
lcd.orient(lcd.LANDSCAPE)
setScreenColor(0x111111)
hat_dlight_0 = hat.get(hat.DLIGHT)
hat_dlight_0.set_mode(0x11)
btnA.wasPressed(buttonA_wasPressed)
btnB.wasPressed(buttonB_wasPressed)

# Constants
lux = None
f_list = [2, 2.8, 4, 5.6, 8, 11, 16]
iso = 400
iso_list = [100, 200, 400, 800, 1600, 3200]

# Initialize UI elements
ui_elements = {
    "titleEv": M5TextBox(5, 5, "EV:", lcd.FONT_DejaVu18, 0xffffff, rotate=0),
    "valueEv": M5TextBox(45, 5, "ev", lcd.FONT_DejaVu18, 0xffffff, rotate=0),
    "titleIso": M5TextBox(100, 5, "ISO:", lcd.FONT_DejaVu18, 0xffffff, rotate=0),
    "valueIso": M5TextBox(150, 5, "iso", lcd.FONT_DejaVu18, 0xffffff, rotate=0),
}

for idx, f_value in enumerate(f_list, start=1):
    xpos = 5 if idx <= 4 else 130
    ypos = 20 * idx if idx <= 4 else 20 * (idx - 4)
    ui_elements["titleF" + str(f_value)] = M5TextBox(xpos, ypos, "F" + str(f_value) + ":", lcd.FONT_DejaVu18, 0xffffff, rotate=0)
    xpos += 60 if idx <= 4 else 55
    ui_elements["valueF" + str(f_value)] = M5TextBox(xpos, ypos, "f" + str(f_value), lcd.FONT_DejaVu18, 0xffffff, rotate=0)


update_ev()
