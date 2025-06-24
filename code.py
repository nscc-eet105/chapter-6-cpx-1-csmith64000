from adafruit_circuitplayground import cp
import time
import random

#pattern
pattern = [0, 4, 8]

#colors
def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return(red, green, blue)

#Loop
while True:
    for pixel in pattern:
        cp.pixels[pixel] = pixel_color()
        time.sleep(0.2)
        cp.pixels[pixel] = (0, 0, 0)




