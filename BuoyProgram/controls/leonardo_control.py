from models.leonardo_model import leonardo_model
from views.buoy_io import buoy_io

'''
leonardo_control - The Arduino Leonardo control class.
'''


class leonardo_control:

    '''
    __init__ - The leonardo_control constructor
    '''

    def __init__(self):

        # __________ Instantiations __________

        # buoy_io instance
        self.io = buoy_io()

        # leonardo_model instance
        self.leonardo = leonardo_model()

    '''
    record_sensings - Records the RFID and temperature
    '''

    def record_sensings(self):

        # Read until a new serial line
        bytes = self.io.getInput(self.leonardo.uart)

        # Decode bytes into string
        line = bytes.decode('utf-8')
        line = line.replace('\r', '').replace('\n', '')

        # Split the data into various elements
        data = line.split(",")

        # Only two elements, RFID and temperature, should be recorded
        if len(data) != 2:
            self.io.display("Invalid input!")
        else:

            # Copy the string information into variables
            self.leonardo.radio_frequency_identification = str(data[0])
            self.leonardo.temperature = str(data[1])

            self.io.display("RFID-Temperature: " +
                            self.leonardo.radio_frequency_identification + ", " + self.leonardo.temperature)
