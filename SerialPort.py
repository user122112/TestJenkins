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

        # Calculator
        ser.write(b'C1 30, 212\r')
        time.sleep(.5)
        ser.write(b'C0\r')
        time.sleep(.5)

        # Calc 7 + 7 = 14
        ser.write(b'C1 4, 67\r')
        time.sleep(.5)
        ser.write(b'C0\r')
        time.sleep(.5)

        time.sleep(.3)
        ser.write(b'C1 8, 97\r')
        time.sleep(.2)
        ser.write(b'C0\r')




        # Settings : Lights Automation
        ser.write(b'C1 14, 214\r')
        time.sleep(.5)
        ser.write(b'C0\r')
        time.sleep(.5)

        # Cart Lights "TOP"-ON
        time.sleep(.7)
        ser.write(b'C1 4, 170\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Cart Lights "TOP"-OFF
        time.sleep(.7)
        ser.write(b'C1 4, 107\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Cart Lights "Keyboard"-ON
        time.sleep(.7)
        ser.write(b'C1 4, 170\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Cart Lights "Keyboard"-OFF
        time.sleep(.7)
        ser.write(b'C1 4, 170\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Cart Lights "Floor"-ON
        time.sleep(.7)
        ser.write(b'C1 4, 243\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Cart Lights "Floor"-OFF
        time.sleep(.7)
        ser.write(b'C1 4, 243\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Cart Lights "All"-ON
        time.sleep(.7)
        ser.write(b'C1 25, 70\r')
        time.sleep(.7)
        ser.write(b'C0\r')

        # Cart Lights "All"-OFF
        time.sleep(.7)
        ser.write(b'C1 25, 70\r')
        time.sleep(.7)
        ser.write(b'C0\r')
        # Lights Back Arrow Press
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

        # Drawer Icon Press
        time.sleep(3)
        ser.write(b'C1 29, 195\r')
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

        # Drawer Back
        time.sleep(3)
        ser.write(b'C1 3, 27\r')
        time.sleep(.2)
        ser.write(b'C0\r')
        time.sleep(3)

        # THIS IS THE GCT CODE
        # GCT Memory Values

        # G0 - GCT System Status Register address 40001
        ser.write(b'G0\r')

        # G1 - GCT Status Registers addresses 40010 – 40013
        ser.write(b'G1\r')

        # G2 - GCT Configuration Registers - address 40080 – 40125
        ser.write(b'G2\r')

        # G3 - GCT Error Registers addressed 40040 – 40045
        ser.write(b'G3\r')

        # G4 - GCT Time Series Registers addresses 40140 – 40188
        ser.write(b'G4\r')

        # G5: Use snapshot 1 for test data
        # ser.write(b'G5\r')

        # G6: Use snapshot 2 for test data
        # ser.write(b'G6\r')

        # G7: Use snapshot 3 for test data
        # ser.write(b'G7\r')

        # G10: Sleep power down command
        # ser.write(b'G10\r')

        # G11: Boot-loader command: Enter bootloader
        # ser.write(b'G11\r')

        # G12: Boot-loader command: query if in bootloader
        #  ser.write(b'G12\r')

        # G13: Boot-loader command: exit bootloader
        # ser.write(b'G13\r')

        # G14: Firmware update command: pay-load command (not implemented)
        # ser.write(b'G14\r')

        # G15: Command to set fan mode off
        ser.write(b'G15\r')

        # G16: Command to set fan mode on
        ser.write(b'G15\r')

        # G17: Command to set charge/discharge mode sequential
        # ser.write(b'G16\r')

        # G18: Command to set charge/discharge mode simultaneous
        # ser.write(b'G18\r')

        # G19: Command to set charge/discharge mode auto
        # ser.write(b'G19\r')

        # N : dump Pin-Code cache
        ser.write(b'N\r')

        # N2 : publish Topic: [events/pin-code] [syncStart]
        ser.write(b'N2\r')

        # N3 : solicit fresh publish of CONFIG topic from cloud
        ser.write(b'N3\r')

        # N4 : publish Topic: [events/pin-code] [syncErrorBadCrc]
        ser.write(b'N4\r')

        # N5 : publish Topic: [events/pin-code] [syncErrorTimeOut
        ser.write(b'N5\r')

        # N6 : publish Topic: [events/pin-code] [syncErrorOther]
        ser.write(b'N6\r')

        # N7 : publish Topic: [events/pin-code] [syncSuccess]
        ser.write(b'N7\r')


# Starts Reading Thread

threading.Thread(target=a).start()

# Starts Writing Thread

threading.Thread(target=b).start()

# Closes serial port. We will put this command at the end of the write command, most likely.
# ser.close()
