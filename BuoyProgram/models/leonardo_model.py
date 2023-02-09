import serial

'''
leonardo_model - The Arduino Leonardo model. 
'''


class leonardo_model:

    '''
    __init__ - The leonardo_model constructor
    '''

    def __init__(self):

        # __________ Initializations __________

        # USB / serial port
        self.serial_port_name = "/dev/ttyACM0"

        # Leonardo inputs
        self.radio_frequency_identification = -1  # Recorded as a RFID
        self.temperature = -1                     # Recorded in Fahrenheit

        # __________ Instantiations __________

        # Serial port instance
        self.uart = serial.Serial(
            self.serial_port_name, baudrate=9600, timeout=10)

    '''
    get_rfid - Get the RFID
    '''

    def get_rfid(self):

        return self.radio_frequency_identification

    '''
    get_temperature - Get the temperature
    '''

    def get_temperature(self):

        return self.temperature
