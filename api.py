import falcon
import json
from db import *

api = application = falcon.API()


class Curse:
    def on_get(self, req, resp):
        query = ''
        if db_type == 'mysql':
            query = '''SELECT * FROM bad_lang ORDER BY RAND() LIMIT 1'''
        elif db_type == 'sqlite':
            query = '''SELECT * FROM bad_lang ORDER BY RANDOM() LIMIT 1'''
        c.execute(query)
        r = c.fetchone()

        print(r)
        resp.body = json.dumps({
            'hey': r[3],
            'language': r[1],
        },
            ensure_ascii=False).encode('utf8').decode()
        resp.status = falcon.HTTP_200


api.add_route('/get_cursed', Curse())
