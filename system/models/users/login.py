class Login:
    def __init__(self, user_id: int, user_name: str, password: str, is_admin: bool, error: str):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin
        self._error = error

    def check_user(self, user_name, password):
        print (self._user_name)
        if self._user_name == user_name and self._password == password:
            print("Success")
        else:
            print(self._error)
