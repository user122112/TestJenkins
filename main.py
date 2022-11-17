# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import serial
import threading
import time

# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

ser = serial.Serial()
ser.port = 'COM5'
ser.baudrate = 115200

ser.open()

# Opens serial port, prints out everything it reads.


def a():
    while ser.is_open:
        data = ser.readline()
        print(data.decode().strip())
        logger.debug(data)

# Sends bit commands (b) to the CCU, then adds a new line message (\r).
# TODO: Add sections for various functions. Maybe try catches? Or writing to the same log as before with the tests we
#  were trying to do.


def b():

    # Currently, this 'For Loop' runs this command five times. Will probably run it twice, once all the
    # functions have been written
    for i in range(5):

        # Sleep lets us wait between commands. I'd recommend using a sleep command between all C1 and C0 commands.
        # C1: Press at location X, Y
        # C0: Release Press

        time.sleep(3)

        # Lights Icon Press

        ser.write(b'C1 5, 214\r')
        time.sleep(.5)
        ser.write(b'C0\r')
        time.sleep(.5)

        # Lights "TOP"-ON
        time.sleep(.7)
        ser.write(b'C1 4, 170\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Lights "TOP"-OFF
        time.sleep(.7)
        ser.write(b'C1 4, 107\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Lights "Keyboard"-ON
        time.sleep(.7)
        ser.write(b'C1 4, 170\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Lights "Keyboard"-off
        time.sleep(.7)
        ser.write(b'C1 4, 170\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Lights "Floor"-ON
        time.sleep(.7)
        ser.write(b'C1 4, 243\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Lights "Floor"-OFF
        time.sleep(.7)
        ser.write(b'C1 4, 243\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Lights "All"-ON
        time.sleep(.7)
        ser.write(b'C1 25, 70\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Lights "All"-OFF
        time.sleep(.7)
        ser.write(b'C1 25, 70\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Lights Back Arrow
        time.sleep(3)
        ser.write(b'C1 3, 27\r')
        time.sleep(.2)
        ser.write(b'C0\r')
        time.sleep(3)

        # Drawer Icon Press
        time.sleep(3)
        ser.write(b'C1 17, 207\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # PASSCODE
        time.sleep(.3)
        ser.write(b'C1 7, 125\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        time.sleep(.3)
        ser.write(b'C1 15, 125\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        time.sleep(.3)
        ser.write(b'C1 25, 125\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        time.sleep(.3)
        ser.write(b'C1 35, 125\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        time.sleep(.3)
        ser.write(b'C1 43, 125\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        time.sleep(.3)
        ser.write(b'C1 7, 226\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Drawer Enter
        time.sleep(.3)
        ser.write(b'C1 43, 76\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Drawer Open
        time.sleep(.3)
        ser.write(b'C1 8, 97\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        time.sleep(.3)
        ser.write(b'C1 18, 97\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        time.sleep(.3)
        ser.write(b'C1 8, 145\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        time.sleep(.3)
        ser.write(b'C1 19, 145\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Drawer Back Arrow
        time.sleep(3)
        ser.write(b'C1 3, 27\r')
        time.sleep(.2)
        ser.write(b'C0\r')
        time.sleep(3)

        # Calculator
        ser.write(b'C1 30, 212\r')
        time.sleep(.5)
        ser.write(b'C0\r')
        time.sleep(.5)

        # Calc Sums 7 + 7 = 14
        ser.write(b'C1 4, 62\r')
        time.sleep(.5)
        ser.write(b'C0\r')
        time.sleep(.5)

        # 7
        time.sleep(.3)
        ser.write(b'C1 26, 187\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # +
        time.sleep(.3)
        ser.write(b'C1 4, 62\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # 7
        time.sleep(.3)
        ser.write(b'C1 26, 244\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # =
        time.sleep(3)
        ser.write(b'C1 2, 24\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Back Arrow
        time.sleep(3)
        ser.write(b'C1 3, 27\r')
        time.sleep(.2)
        ser.write(b'C0\r')
        time.sleep(3)
        
        # Drawer Up
        ser.write(b'C1 41, 183\r')
        time.sleep(.7)
        ser.write(b'C0\r')
        time.sleep(.7)

        # Drawer Down
        ser.write(b'C1 41, 102\r')
        time.sleep(.7)
        ser.write(b'C0\r')
        time.sleep(.7)

        # Settings Icon
        time.sleep(.3)
        ser.write(b'C1 45, 30\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Display Brightness
        time.sleep(.3)
        ser.write(b'C1 17, 42\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Back Arrow
        time.sleep(.3)
        ser.write(b'C1 2, 30\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # System Information
        time.sleep(.3)
        ser.write(b'C1 16, 97\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Back Arrow
        time.sleep(.3)
        ser.write(b'C1 2, 30\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Time Configuration
        time.sleep(.3)
        ser.write(b'C1 14, 137\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Back Arrow
        time.sleep(.3)
        ser.write(b'C1 2, 30\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # About
        time.sleep(.3)
        ser.write(b'C1 22, 186\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Back Arrow
        time.sleep(.3)
        ser.write(b'C1 2, 30\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Mac
        time.sleep(.3)
        ser.write(b'C1 22, 223\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Back Arrow
        time.sleep(.3)
        ser.write(b'C1 2, 30\r')
        time.sleep(.2)
        ser.write(b'C0\r')

        # Close
        time.sleep(.3)
        ser.write(b'C1 43, 38\r')
        time.sleep(.2)
        ser.write(b'C0\r')

# Starts Reading Thread
# es 

threading.Thread(target=a).start()

# Starts Writing Thread

threading.Thread(target=b).start()

# Closes serial port. We will put this command at the end of the write command, most likely.
# ser.close()
