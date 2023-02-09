import datetime
import mysql.connector


'''
my_SQL_database - The mySQL database model.
'''


class database_model:

    '''
    __init__ - The my_SQL_database constructor
    '''

    def __init__(self):

        # __________ Instantiations __________

        # mySQL database instance
        self.database = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="dstK98!harrdayt22",
            database="buoy_database",
        )

        # Cursor instance
        self.cursor = self.database.cursor()

    '''
    get_time - Get the local time
    '''

    def get_time(self):

        return datetime.datetime.now().strftime("%H:%M:%S")
