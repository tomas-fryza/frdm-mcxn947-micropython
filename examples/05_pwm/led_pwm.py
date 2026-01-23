from machine import PWM, Pin
import time

SATURATION = 1
VALUE = 0.2

ledr = Pin('P0_10', Pin.OPEN_DRAIN, value=1)
ledg = Pin('P0_27', Pin.OPEN_DRAIN, value=1)
ledb = Pin('P1_2',  Pin.OPEN_DRAIN, value=1)

p_ledr = PWM(ledr, freq=1000, duty_u16=0, invert=True)
p_ledg = PWM(ledg, freq=1000, duty_u16=0, invert=True)
p_ledb = PWM(ledb, freq=1000, duty_u16=0, invert=True)

def led_color(r, g, b):
    p_ledr.duty_u16(int(r * 65536 / 256))
    p_ledg.duty_u16(int(g * 65536 / 256))
    p_ledb.duty_u16(int(b * 65536 / 256))

def hsv_to_rgb(h, s, v):
    var_c = v * s
    var_x = var_c * (1 - abs(((h / 60) % 2) - 1))
    var_m = v - var_c

    r_t, g_t, b_t = 0, 0, 0

    if h < 60:
        r_t, g_t, b_t = var_c, var_x, 0
    elif h < 120:
        r_t, g_t, b_t = var_x, var_c, 0
    elif h < 180:
        r_t, g_t, b_t = 0, var_c, var_x
    elif h < 240:
        r_t, g_t, b_t = 0, var_x, var_c
    elif h < 300:
        r_t, g_t, b_t = var_x, 0, var_c
    elif h < 360:
        r_t, g_t, b_t = var_c, 0, var_x

    r = (r_t + var_m) * 255
    g = (g_t + var_m) * 255
    b = (b_t + var_m) * 255

    return r, g, b

while(True):
    for i in range(360):
        r, g, b = hsv_to_rgb(i, SATURATION, VALUE)
        led_color(r, g, b)
        time.sleep_ms(25)