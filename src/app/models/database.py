# import psycopg2 as pgsql
import sqlite3


class DBConnect:
    def __init__(self):
        # Connection to SQLite
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

        # Connection to PostgreSQL
        # self.connection = pgsql.connect(dbname='postgres',
        #                                 user='postgres',
        #                                 password='postgres',
        #                                 host='localhost',
        #                                 port=5432)
        # self.connection.autocommit = True
        # self.cursor = self.connection.cursor()
