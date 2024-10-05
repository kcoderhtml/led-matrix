from max7219 import Matrix8x8
from machine import Pin, SPI
from utime import sleep

CS = Pin(5, Pin.OUT) # GPIO5 pin 7
CLK = Pin(6) # GPIO6 pin 9
DIN = Pin(7) # GPIO7 pin 10

text = "VISITE O CANAL BRINQUEDOS MAKER NO YOUTUBE"

# CLK = GPIO6 and MOSI (DIN) = GPIO7 are the default pins of SPI0 so you can omit it
spi = SPI(0, baudrate= 10_000_000,  sck=CLK, mosi=DIN)
display = Matrix8x8(spi, CS, 1, orientation=1)

while True:

    # show a string scrolling through the Matrix
    display.text_scroll(text)