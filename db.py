import MySQLdb


class DB:
    def __init__(self, host='localhost', user='root', passwd='123456', db='main', port=3306):
        self.conn = MySQLdb.connect(host, user, passwd, db, port)
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

