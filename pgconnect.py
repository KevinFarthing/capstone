import psycopg2 as pg2
import datetime
# from login import postgres_config
from psycofunctions import add_story, get_story, drop_old, get_titles
import os

# added uber_id 22 as test

def connect(x=None, l1=None):
    """ Connect to the PostgreSQL database server \n
    x = psyco function to use\n
    y = list of variables psycofunction will need"""
    conn = None
    y=None
    try:
        # read connection parameters
        # params = postgres_config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # try:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = pg2.connect(DATABASE_URL)
        # except KeyError:
        #     DATABASE_URL = 'writing_prompt'
        #     conn = pg2.connect(database=DATABASE_URL, user='kevin', password='admin')
        # conn = pg2.connect(**params sslmode="require") #?SSL mode?

        # create a cursor
        cur = conn.cursor()
        
 # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        # display the PostgreSQL database server version
        if x:
            y = x(conn, l1)
            conn.commit()
       
     # close the communication with the PostgreSQL
        cur.close()

    except (Exception, pg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    if y:
        return y
 
# ???
if __name__ == '__main__':
    connect()


