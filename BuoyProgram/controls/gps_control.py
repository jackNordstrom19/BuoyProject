from models.gps_model import gps_model
from views.buoy_io import buoy_io

import time


'''
gps_control - The Adafruit Ultimate Global Positioning System control class.
'''


class gps_control:

    '''
    __init__ - The gps_control constructor
    '''

    def __init__(self):

        # __________ Instantiations __________

        # buoy_io instance
        self.io = buoy_io()

        # gps_model instance
        self.gps = gps_model()

    '''
    fixate_connection - Fixate the connection to the satellite
    '''

    def fixate_connection(self):

        # __________ Initializations __________

        # Time instance variables recorded in monotonic time
        self.time_current = -1
        self.time_last = -1

        # Turn on basic GGA and RMC information
        self.gps.gps.send_command(
            b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

        # Set update rate to once every 1000 millisecond or 1Hz
        self.gps.gps.send_command(b"PMTK220,1000")

        # Store monotonic time to the last time initially
        self.time_last = time.monotonic()

        # Loop until the GPS has a fixation on the satellites
        while True:

            # Update the gps information
            self.gps.gps.update()

            # Store monotonic time to the current time
            self.time_current = time.monotonic()

            # Print out input if a second has passed and thus the GPS has a fix
            if self.time_current - self.time_last >= 1.0:
                self.time_last = self.time_current

                # Print out message to show GPS doesn't have a fix
                if not self.gps.gps.has_fix:
                    self.io.display("Waiting for satellite fixation...")
                    continue

                self.io.display("Satellite connection found!")

                return True

    '''
    record_position - Records the latitude and longitude 
    '''

    def record_position(self):

        # Limit the decimal places of latitude and longitude
        self.gps.latitude = "{:.6f}".format(self.gps.gps.latitude)
        self.gps.longitude = "{:.6f}".format(self.gps.gps.longitude)

        # Convert from a float to a string
        self.gps.latitude = str(self.gps.latitude)
        self.gps.longitude = str(self.gps.longitude)

        self.io.display("Latitude-Longitude: " +
              self.gps.latitude + ", " + self.gps.longitude)
