#!/usr/bin/python
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class DB():
    def __init__(self, tablename, hostname = 'localhost', port = '5432', username = 'postgres',
                password = 'postgres'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.tablename = tablename
        self.connection = self._get_connection()
        self._make_table()

    def run_psql(self, cmd):
        cur = self.connection.cursor()
        cur.execute(cmd)
        self.connection.commit()
        try:
            return cur.fetchall()
        except:
            pass
    
    def _create_tables(self, tablename) :
        """ create tables in the PostgreSQL database"""
        cur = self.connection.cursor()
        cur.execute(f'CREATE TABLE {tablename} (arrival_time timestamp PRIMARY KEY, transmit_time timestamp, count int NOT NULL)')
        self.connection.commit()

    def init_database(self, name) :
        cur = self.connection.cursor()
        cur.execute( f"SELECT datname FROM pg_catalog.pg_database WHERE datname = '{name}'" )
        dbs = []
        for firstname in cur.fetchall() :
            for name in firstname :
                print( name )
                dbs.append(name)
        if not name in dbs :
            print(f'database {name} not found')
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = self.connection.cursor()
            cur.execute( f'CREATE DATABASE {name};' )
            cur.execute( f"SELECT datname FROM pg_catalog.pg_database WHERE datname = '{name}'" )
            print(cur.fetchall())

    def _get_tables(self):
        self.connection = psycopg2.connect( host=self.hostname, user=self.username, password=self.password )
        cmd =   f"""
                 SELECT table_name
                 FROM information_schema.tables
                 WHERE table_schema = 'public'
                 ORDER BY table_name;
                 """

        cur = self.connection.cursor()
        cur.execute( cmd )
        tables = []
        for row in cur.fetchall():
            tables.append(row[0])
        return tables

    def _get_connection(self):
        connection = psycopg2.connect( host=self.hostname, user=self.username, password=self.password, port=self.port)
        return connection

    def _make_table(self):   
        if not self.tablename in self._get_tables():
            print(f'table {self.tablename} not found in db creating..' )
            self._create_tables(self.tablename)
        else:
            print(f'table {self.tablename} found in db' )
