import psycopg2
import wget
import config


connection = psycopg2.connect(host=config.hostname, dbname=config.databname, user=config.username, password=config.passw)
cursor = connection.cursor()

def sel(a):
    s_query = f"""SELECT * FROM public.parser WHERE id = {a}"""
    print(cursor.execute(s_query))
    return cursor.fetchone()

print(sel(10))