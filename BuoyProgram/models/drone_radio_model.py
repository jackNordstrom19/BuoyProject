from digi.xbee.devices import Raw802Device
from digi.xbee.devices import RemoteRaw802Device
from digi.xbee.devices import XBee64BitAddress

'''
drone_radio_model - The Digi Xbee Pro S1 model.
'''


class drone_radio_model:

    '''
    __init__ - The drone_radio_model constructor
    '''

    def __init__(self):

        # __________ Initializations __________

        # Local radio USB / serial
        self.local_radio = Raw802Device("/dev/ttyUSB0", 9600)

        # Set timeout of local radio
        self.local_radio.set_sync_ops_timeout(5)

        # Remote radio 64 bit address
        self.remote_radio = RemoteRaw802Device(
            self.local_radio, XBee64BitAddress.from_hex_string("0013A20041905101"))
