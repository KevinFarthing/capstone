from configparser import ConfigParser
import os

 
 
def postgres_config(filename='data.ini', section='postgresql'):
    
    parser = ConfigParser()
    parser.read(filename)

 
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        try:
            DATABASE_URL = os.environ['DATABASE_URL'] # os.getenv()
            db['database'] = DATABASE_URL
        except KeyError:
            pass
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

def reddit_config(filename='data.ini', section='reddit'):
    parser = ConfigParser()
    parser.read(filename)
 
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

