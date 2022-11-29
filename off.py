# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import neopixel
import time

npix = 144
pixels = neopixel.NeoPixel(board.GP0, npix)

#pixels[0] = (20,0,0)
#pixels[-1] = (0,20,0)

for i in range(npix):
    pixels[i] = (0,0,0)
