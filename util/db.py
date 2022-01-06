import pymysql
from queue import Queue

class SQLPool:
    def __init__(self, num, _host='localhost', _user='root', _password='123456', _database='longx', _port=3306):
        self.conns = Queue()
        for i in range(num):
            conn = pymysql.connect(host=_host, user=_user, password=_password, database=_database, port=_port)
            self.conns.put(conn)

    def acquire(self):
        conn = self.conns.get()
        conn.ping(reconnect=True)
        return conn

    def release(self, conn):
        self.conns.put(conn)

g_sql_pool = SQLPool(4)

class SQLAdapter:
    def __enter__(self):
        self.conn = g_sql_pool.acquire()
        self.csr = self.conn.cursor()
        return self

    def __exit__(self, tp, val, trc):
        self.csr.close()
        g_sql_pool.release(self.conn)

    def query(self, sql):
        try:
            self.sql = sql
            self.csr.execute(sql)
            data = self.csr.fetchall()
            self.conn.commit()
            col_name = [cols[0] for cols in self.csr.description]
            col_num = len(self.csr.description)
            arr = []
            for row in data:
                kv = {}
                for col in range(col_num):
                    kv[col_name[col]] = row[col]
                arr.append(kv)
            return arr
        except Exception as e:
            return []

    def execute(self, sql):
        sql.sql = sql
        self.csr.execute(sql)

    def commit(self):
        self.conn.commit()

    def rollback():
        self.conn.rollback()
