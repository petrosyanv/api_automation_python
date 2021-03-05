import random
from common.utility import hash_generator


class User:

    def __init__(self, user_name, user_age, user_id=None):
        self.user_id = user_id
        self.user_name = user_name
        self.user_age = user_age

    @staticmethod
    def generate_random():
        age = random.randint(18, 35)
        return User(
            user_name=f'{hash_generator()}',
            user_age=age
        )

    @staticmethod
    def deserialize_from_dict(dict_obj: dict):
        return User(
            user_id=dict_obj.get('id'),
            user_name=dict_obj.get('name'),
            user_age=dict_obj.get('age')
        )

    def serialize_to_dict(self):
        return {
            "id": self.user_id,
            "name": self.user_name,
            "age": self.user_age
        }
