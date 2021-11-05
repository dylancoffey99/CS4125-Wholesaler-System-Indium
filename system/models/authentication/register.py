from system.models.database.db_handler import UserDB

class Register:
    def __init__(self, user_id: int, user_name: str, password: str, is_admin: bool):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin

    def add_user(self, user: UserDB):
        pass

    def get_user(self, user_id: int) -> UserDB:
        pass

    def get_all_users(self) -> List[UserDB]:
        pass

    def ask_user_credentials(self): -> return str:
        print("Please Provide")
        user_name = str(input("Name: "))
        password = str(input("Password: "))
        return user_name, password