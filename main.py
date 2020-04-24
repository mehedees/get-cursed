import os
from db import *


word_list = []
collections_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'collections')
for root, _, files in os.walk(collections_path):
    for file in files:
        with open(os.path.join(root, file), 'r') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
            for l in lines:
                word_list.append((file, l))

query = '''INSERT INTO bad_lang (lang_code, word) VALUES '''

for l in word_list:
    query += (str(l) + ',')

query = query[:-1]
print(query)
r = c.execute(query)
mydb.commit()
mydb.close()
