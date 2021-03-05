import json

from api.controllers.base_controller import BaseController
from api.entities.user import User


class Users(BaseController):

    URI_PREFIX = '/user'

    def create(self, user: User = None):
        if user is None:
            user = User.generate_random()
        body = user.serialize_to_dict()
        response = self.caller.call(method='post', uri=f'{self.URI_PREFIX}/createUser', body=body)
        user.user_id = int(json.loads(response.text)['id'])
        return user.user_id

    def get(self, user_id):
        response = self.caller.call(method='get', uri=f'{self.URI_PREFIX}/getUserById/{user_id}')
        return User.deserialize_from_dict(json.loads(response.text))

    def update(self, user: User):
        body = user.serialize_to_dict()
        response = self.caller.call(method='put', uri=f'{self.URI_PREFIX}/updateUser', body=body)
        return int(json.loads(response.text)['id'])
