from controls.database_control import database_control
from controls.drone_radio_control import drone_radio_control
from controls.gps_control import gps_control
from controls.leonardo_control import leonardo_control
from views.buoy_io import buoy_io

database = database_control()
radio = drone_radio_control()
gps = gps_control()
io = buoy_io()
leonardo = leonardo_control()

io.display("\n")
# gps.fixate_connection()
# gps.record_position()
gps.gps.latitude = 29
gps.gps.longitude = 81
io.display("\n")
io.display("Waiting for sensor scan...")

leonardo.record_sensings()
io.display("\n")

database.store_position(database.database.get_time(),
                        gps.gps.get_latitude(), gps.gps.get_longitude())
database.store_rfid(database.database.get_time(), leonardo.leonardo.get_rfid())
database.store_temperature(
    database.database.get_time(), leonardo.leonardo.get_temperature())
io.display("\n")

io.display("Waiting for radio message...")
message = radio.receive_message()
database.store_rfid(database.database.get_time(), message)


'''
main - The main point of entry into the program.
'''


class main:

    '''
    __init__ - The main constructor
    '''

    def __init__(self):

        pass
