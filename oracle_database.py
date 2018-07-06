import cx_Oracle

CONN_INFO = {
    'host': 'localhost',
    'port': 1521,
    'user': 'source_db',
    'psw': 'oracle',
    'service': 'orcl'
}

CONN_STR = '{user}/{psw}@{host}:{port}/{service}'.format(**CONN_INFO)

QUERY = '''/*create table TEST_MAITYP1 as*/ select * from JOBS '''


class DB:
    """this class is to create connection """

    def __init__(self):
        self.conn = cx_Oracle.connect(CONN_STR)

    def query(self, query):
        cursor = self.conn.cursor()
        result = cursor.execute(query).fetchall()
        cursor.close()
        return result


db = DB()
try:
    result = db.query(QUERY)
    for row in result:
        print(row)
except Exception as e:
    print(e)

else:
    print("No exception found")

finally:
    print('finally:\n')
