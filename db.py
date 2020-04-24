# import MySQLdb
import sqlite3

# db = 'mysql'
db_type = 'sqlite'
# mydb = MySQLdb.connect(host='localhost', user='root', passwd='12345678', database='bad_lang')
mydb = sqlite3.connect(database='bad_lang.db')
c = mydb.cursor()