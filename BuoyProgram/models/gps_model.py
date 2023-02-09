import adafruit_gps
import serial

'''
gps_model - The Adafruit Ultimate Global Positioning System model.
'''


class gps_model:

    '''
    __init__ - The gps_model constructor
    '''

    def __init__(self):

        # __________ Initializations __________

        # USB / serial port
        self.serial_port_name = "/dev/ttyUSB0"

        # GPS inputs recorded in decimal degrees
        self.latitude = -1
        self.longitude = -1

        # __________ Instantiations __________

        # Serial port instance
        self.uart = serial.Serial(
            self.serial_port_name, baudrate=9600, timeout=10)

        # Adafruit gps instance
        self.gps = adafruit_gps.GPS(self.uart, debug=False)

    '''
    get_latitude - Get the latitude
    '''

    def get_latitude(self):

        return self.latitude

    '''
    get_longitude - Get the longitude
    '''

    def get_longitude(self):

        return self.longitude
