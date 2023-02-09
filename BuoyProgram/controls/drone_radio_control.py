from models.drone_radio_model import drone_radio_model
from views.buoy_io import buoy_io

'''
drone_radio_control - The Digi Xbee Pro S1 control class.
'''


class drone_radio_control:

    '''
    __init__ - The drone_radio_control constructor
    '''

    def __init__(self):

        # __________ Instantiations __________

        # buoy_io instance
        self.io = buoy_io()

        # drone_radio_model instance
        self.drone_radio = drone_radio_model()

    '''
    receive_message - Receives a message from the other drone radio
    '''

    def receive_message(self):

        # Open the local radio channel
        self.drone_radio.local_radio.open()

        # Store the received message
        self.message = self.drone_radio.local_radio.read_data(5)

        self.io.display("Radio message received!")

        # Close the local radio channel
        self.drone_radio.local_radio.close()

        return self.message.data.decode("utf8")

    '''
    send_message - Sends a message to the other drone radio
    '''

    def send_message(self):

        # Open the local radio channel
        self.drone_radio.local_radio.open()

        self.drone_radio.local_radio.send_data_64(
            self.drone_radio.remote_radio.get_64bit_addr(), bytearray("987654321", "utf-8"))

        # Close the local radio channel
        self.drone_radio.local_radio.close()
