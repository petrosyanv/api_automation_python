import psycopg2


class DBHelper:

    __connection = None
    __cursor = None

    def __init__(self):
        self.__connection = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='password'")
        self.__cursor = self.__connection.cursor()

    def execute_query(self, query):
        self.__cursor.execute(query)
        items = self.__cursor.fetchall()
        return items

    def execute_without_response(self, query):
        self.__cursor.execute(query)




