# import MySQLdb
import sqlite3
import os

# db = 'mysql'
db_type = 'sqlite'

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bad_lang.db')
# mydb = MySQLdb.connect(host='localhost', user='root', passwd='12345678', database='bad_lang')
mydb = sqlite3.connect(database=db_path)
c = mydb.cursor()