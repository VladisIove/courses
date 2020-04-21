import psycopg2 as psy 
import json 
import os

def migration(host, database, user, password):
    conn = psy.connect(host=host,database=database, user=user, password=password)
    cursor = conn.cursor()
    cursor.execute("select * from information_schema.tables where table_name=%s", ('migrations',))
    if bool(cursor.rowcount):
        cursor.execute('SELECT * FROM migrations ORDER BY id DESC LIMIT 1;')
        last_id = cursor.fetchone()[0]
    else:
        cursor.execute('CREATE TABLE migrations(id serial PRIMARY KEY, command VARCHAR(1024) NOT NULL);')
        last_id = -1
        conn.commit()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) 
    with open(os.path.join(__location__, 'migrations.json')) as json_file:
        data = json.load(json_file)
        for d in data:
            if d["id"] > last_id:
                cursor.execute(d["command"])
                cursor.execute("INSERT INTO migrations (command) VALUES ('{}')".format(d["command"]))
                conn.commit() 
    cursor.close()
    conn.close()




