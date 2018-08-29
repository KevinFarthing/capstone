import datetime
from random import randint

def get_titles(conn, l1):
    with conn.cursor() as curr:
        curr.execute("SELECT prompt_text FROM main_view;")
        record = curr.fetchall()
    return [str(each[0]) for each in record]

def get_full_list(conn, l1):
    with conn.cursor() as curr:
        curr.execute("SELECT prompt_text, url, uber_id FROM main_view;")
        record = curr.fetchall()
    return record # duh. this also works.

def get_ids(conn, l1=[]):
    with conn.cursor() as curr:
        curr.execute("SELECT uber_id FROM uber;")
        record = curr.fetchall()
    return [each[0] for each in record]

def get_story(conn, id):
    with conn.cursor() as curr:
        curr.execute(f"SELECT * FROM main_view WHERE uber_id = {id};")
        record = curr.fetchone()
    return record

def get_random_story(conn,l1):
    ids = get_ids(conn)
    # i = randint(0,len(ids)-1)
    i = ids[randint(0,len(ids)-1)]
    record = get_story(conn,i)
    return record
    


def add_story(conn, l1):
    with conn.cursor() as curr: 
        curr.execute(f"SELECT * FROM add_story('{l1[0]}','{l1[1]}','{l1[2]}','{l1[3]}','{l1[4]}')")

def drop_old(conn, l1):
    # ought to be a function stored in server but testing
    with conn.cursor() as curr:
        curr.execute(f"SELECT * FROM uber")
        records = curr.fetchall()
    for record in records:
        if datetime.date.today() - record[6] > datetime.timedelta(days=3) and not record[4]:
            with conn.cursor() as local_curr:
                local_curr.execute(f"DELETE FROM prompt WHERE prompt_id={record[1]};")
                local_curr.execute(f"DELETE FROM story WHERE story_id={record[3]};")
                local_curr.execute(f"DELETE FROM uber WHERE uber_id={record[0]};")
            print("Removed uber_id " + str(record[0]))

    # create new view of id's, then do drops for each table - author, story, prompt, uber
    # DELETE FROM table_name WHERE condition; - base

