from models.database_model import database_model
from views.buoy_io import buoy_io


'''
my_SQL_database_control - The mySQL database model control class.
'''


class database_control:

    '''
    __init__ - The mySQL database constructor
    '''

    def __init__(self):

        # __________ Instantiations __________

        # buoy_io instance
        self.io = buoy_io()

        # database_model instance
        self.database = database_model()

    '''
    store_position - Store position input into the database
    '''

    def store_position(self, time, latitude, longitude):

        # Insert input into database
        self.database.cursor.execute(
            "INSERT INTO buoy_position (Time, Latitude, Longitude) VALUES (%s, %s, %s)", (time, latitude, longitude))

        # Commit the change made to the database
        self.database.database.commit()

        self.io.display("Position stored into database!")

    '''
    store_rfid - Store RFID input into the database
    '''

    def store_rfid(self, time, rfid):

        # Insert input into database
        self.database.cursor.execute(
            "INSERT INTO buoy_RFID (Time, RFID) VALUES (%s, %s)", (time, rfid))

        # Commit the change made to the database
        self.database.database.commit()

        self.io.display("RFID stored into database!")

    '''
    store_temperature - Store temperature input into the database
    '''

    def store_temperature(self, time, temperature):

        # Insert input into database
        self.database.cursor.execute(
            "INSERT INTO buoy_temperature (Time, Temperature) VALUES (%s, %s)", (time, temperature))

        # Commit the change made to the database
        self.database.database.commit()

        self.io.display("Temperature stored into database!")
