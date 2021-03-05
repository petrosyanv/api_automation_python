from api.database.db_helper import DBHelper


class BaseDao:

    __db = None

    def __init__(self):
        self.__db = DBHelper()

    def get_users(self):
        return self.__db.execute_query('SELECT * FROM users')

    def get_user_by_id(self, id):
        return self.__db.execute_query(f'SELECT * FROM users WHERE id = {id}')

    def delete_user_by_id(self, id):
        return self.__db.execute_without_response(f'DELETE FROM users WHERE id = {id}')


if __name__ == "__main__":
    dao = BaseDao()
    a = dao.get_users()
    for i in a:
        print(i)
