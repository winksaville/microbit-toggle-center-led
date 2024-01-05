# Turn on the center display LED when Button A is pressed
from microbit import *

PIXEL_LEVEL_MAX_ON: int = 9
PIXEL_LEVEL_MIN_ON: int = 1
PIXEL_LEVEL_OFF: int = 0

PIXEL_ON: int = PIXEL_LEVEL_MAX_ON
PIXEL_OFF: int = PIXEL_LEVEL_OFF

# Center Pixel
PIXEL_X: int = 2
PIXEL_Y: int = 2

# Set initial conditions
print("Starting with pixel off");
display.set_pixel(PIXEL_X, PIXEL_Y, PIXEL_OFF)
prev_pixel_state: int = PIXEL_OFF

# Loop changing pixel state when button is pressed or released
while True:
    if button_a.is_pressed():
        display.set_pixel(PIXEL_X, PIXEL_Y, PIXEL_ON)
        if prev_pixel_state == PIXEL_OFF:
            print("Pixel is on")
            prev_pixel_state = PIXEL_ON
    else:
        display.set_pixel(PIXEL_X, PIXEL_Y, PIXEL_OFF)
        if prev_pixel_state == PIXEL_ON:
            print("Pixel is off")
            prev_pixel_state = PIXEL_OFF
