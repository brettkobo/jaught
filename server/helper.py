import sqlite3
import uuid
import datetime
import time
import json

DB_PATH = "./server/jaught.db"  # Update this path accordingly


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))
        conn.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None


def add_to_notes(title, body, tags):
    try:
        conn = sqlite3.connect(DB_PATH)

        note_id = str(uuid.uuid4())
        collection_id = str(uuid.uuid4())
        creation_date = int(time.time())
        modified_date = int(time.time())

        c = conn.cursor()

        c.execute(
            'insert into notes(note_id, title, body, tags, collection_id, creation_date, modified_date) values(?,?,?,?,?,?,?)',
            (note_id, title, body, json.dumps(tags), collection_id, creation_date, modified_date)
        )
        conn.commit()
        return {"note_id": note_id,
                "title": title,
                "body": body,
                "tags": tags,
                "collection_id": collection_id,
                "creation_date": creation_date,
                "modified_date": modified_date,
                }
    except Exception as e:
        print('Error: ', e)
        return None


def get_all_notes():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = dict_factory

        sql_command = """
        select 
        note_id, 
        title, 
        body, 
        tags, 
        collection_id, 
        creation_date,
        modified_date
        from notes 
        order by creation_date DESC
        """
        # json_extract(test, '$.tags')
        c = conn.cursor()
        c.execute(sql_command)
        rows = c.fetchall()
        return {"count": len(rows), "items": rows}
    except Exception as e:
        print('Error: ', e)
        return None


def remove_note(note_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('DELETE FROM notes WHERE note_id=?', (note_id,))
        conn.commit()

    except Exception as e:
        print('Error: ', e)
        return None
