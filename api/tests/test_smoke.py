from api.database.base_dao import BaseDao
from api.entities.api_client import ApiClient
from api.entities.user import User


class TestSmoke:

    @classmethod
    def setup_class(cls):
        cls.api_client = ApiClient()
        cls.dao = BaseDao()

    def test_api_update(self):
        create_user = User.generate_random()
        user_id = self.api_client.users.create(create_user)
        try:
            updated_decedent = User.generate_random()
            updated_decedent.user_id = user_id
            updated_user_id = self.api_client.users.update(user=updated_decedent)
            assert updated_user_id == user_id, \
                'User ID from PUT / User/id differs from User ID from POST /Users'
            actual_user = self.dao.get_user_by_id(updated_user_id)
            assert actual_user[0][2] == updated_decedent.user_name, \
                'User ID from POST / User/was not updated User ID from POST /Users'
        finally:
            self.dao.delete_user_by_id(user_id)