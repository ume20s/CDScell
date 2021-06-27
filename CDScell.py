import wiringpi as pi
import time
import subprocess

SPI_CH = 0
READ_CH = 0
state = 0

pi.wiringPiSPISetup(SPI_CH, 1000000 )

while True:
    buffer = 0x6800 |  (0x1800 * READ_CH ) 
    buffer = buffer.to_bytes( 2, byteorder='big' )

    pi.wiringPiSPIDataRW( SPI_CH, buffer )
    value = ( buffer[0] * 256 + buffer[1] ) & 0x3ff

    if (value > 500) and (state == 1):
        print ("Bright")
        subprocess.call("aplay oha.wav", shell=True)
        state = 0
    elif(value < 500) and (state == 0):
        print ("Dark")
        subprocess.call("aplay oya.wav", shell=True)
        state = 1

    time.sleep(1)
