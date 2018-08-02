import datetime
from random import randint

def get_titles(conn, l1):
    with conn.cursor() as curr:
        curr.execute("SELECT prompt_text FROM main_view;")
        record = curr.fetchall()
    return [str(each[0]) for each in record]

def get_ids(conn, l1=[]):
    with conn.cursor() as curr:
        curr.execute("SELECT uber_id FROM uber;")
        record = curr.fetchall()
    return [each[0] for each in record]

def get_story(conn, l1):
    with conn.cursor() as curr:
        ids = get_ids(conn)
        i = randint(0,len(ids)-1)
        curr.execute(f"SELECT * FROM main_view WHERE uber_id = {ids[i]};")
        # curr.execute(f"SELECT * FROM main_view;")
        record = curr.fetchone() # returns the tuples without looping! .fetchall() returns a list of tuples.
        # prompt_author = record[1]
        # story_author = record[2]
        # prompt_text = record[3]
        # story_text = record[4]
    # oh shit, fetch REMOVES FROM CURSOR like .pop
    # print(len(curr.fetchall()))
    # for record in curr:
    #     # record creates a tuple of  
    return record

# print(curr[0][1])

# okay, easy. just need to pass this to a flask app.

# don't forget, prompt text and story text need to be cleared of double quotes and all single quotes switched to repeats.
def add_story(conn, l1):
    with conn.cursor() as curr: 
        curr.execute(f"SELECT * FROM add_story('{l1[0]}','{l1[1]}','{l1[2]}','{l1[3]}','{l1[4]}')")

def drop_old(conn, l1):
    with conn.cursor() as curr:
        curr.execute(f"SELECT * FROM uber")
        records = curr.fetchall()
    for record in records:
        if datetime.date.today() - record[6] > datetime.timedelta(days=6) and not record[4]:
            with conn.cursor() as local_curr:
                print(f"DELETE FROM prompt WHERE prompt_id={record[1]};")
                local_curr.execute(f"DELETE FROM prompt WHERE prompt_id={record[1]};")
                print(f"DELETE FROM story WHERE story_id={record[3]};")
                local_curr.execute(f"DELETE FROM story WHERE story_id={record[3]};")
                print(f"DELETE FROM uber WHERE uber_id={record[0]};")
                local_curr.execute(f"DELETE FROM uber WHERE uber_id={record[0]};")
            print("Removed uber_id " + str(record[0]))

    # create new view of id's, then do drops for each table - author, story, prompt, uber
    # DELETE FROM table_name WHERE condition; - base

