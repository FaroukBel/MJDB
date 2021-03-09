import mysql.connector
import socket

host = socket.gethostname()
host_ip = socket.gethostbyname(host)


class MyCursor(object):
    def __init__(self):
        super(MyCursor, self).__init__()
        self.db = mysql.connector.connect(
            host=host_ip,
            user='agence',
            port='3306',
            passwd='',
            database='mjdbdatabase'
        )
        self.mycursor = self.db.cursor()

