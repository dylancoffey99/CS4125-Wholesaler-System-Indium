from system.models.database.db_handler import UserDB

class Login:
    def init(self, user: UserDB):
        self._user = user
        self._user_db = UserDB("userDB")

    def check_user(self, user_name, password):
        print (self._user_name)
        if self._user_name == user_name and self._password == password:
            print("Success")
        else:
            print(self._error)