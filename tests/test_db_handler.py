from system.models.users.user import User
from system.database.db_handler import UserDB


class TestUserDB:
    mock_db = UserDB("testUserDB")
    mock_user = User("username", "password", 0, 1)

    def test_add_user(self):
        pass

    def test_get_user(self):
        pass

    def test_get_all_users(self):
        pass

    def test_user_exists(self):
        pass
