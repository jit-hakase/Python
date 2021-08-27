import pymysql

class DB:
    def __init__(self, _host='localhost', _user='root', _password='123456', _database='main', _port=3306):
        self.conn = pymysql.connect(host=_host, user=_user, password=_password, database=_database, port=_port)
        self.csr = self.conn.cursor()

    def execute(self, sql):
        try:
            self.csr.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def query(self, sql):
        try:
            self.csr.execute(sql)
            data = self.csr.fetchall()
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
            print(e)
            return []
