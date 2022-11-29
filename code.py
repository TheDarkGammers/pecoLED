# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import neopixel
import time

npix = 20
pixels = neopixel.NeoPixel(board.GP0, npix)

#pixels[0] = (20,0,0)
#pixels[-1] = (0,20,0)

# for i in range(10,30):
#     pixels[i] = (10,0,0)
# for i in range(40,60):
#     pixels[i] = (0,20,0)

for i in range(npix):
    pixels[i] = (10,0,0)
    pixels[i-2] = (0,0,0)
    pixels[i-4] = (0,10,0)
    pixels[i-6] = (0,0,0)
    time.sleep(0.25)

