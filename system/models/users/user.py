import hashlib
import os


class User:
    def __init__(self, user_id: int, user_name: str, password: str, is_admin: bool):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin

    def get_user(self):
        return [self._user_id, self._user_name, self._password, self._is_admin]

    def get_user_id(self):
        return self._user_id

    def get_user_name(self):
        return self._user_name

    def get_password(self):
        return self._password

    def get_is_admin(self):
        return self._is_admin

    def set_user(self, user_name: str, password: str):
        self._user_name = user_name
        self._password = self.get_hashed_password(password)

    def get_hashed_password(self, password: str) -> str:
        # https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
        # https://stackoverflow.com/questions/48448830/hashing-password-in-py-file
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            'sha256',  # The hash digest algorithm for HMAC
            password.encode('utf-8'),  # Convert the password to bytes
            salt,  # Provide the salt
            100000  # It is recommended to use at least 100,000 iterations of SHA-256
        )
        # Store them as:
        storage = salt + key

        # Getting the values back out
        salt_from_storage = storage[:32]  # 32 is the length of the salt
        key_from_storage = storage[32:]

        salt_and_key = [salt_from_storage, key_from_storage]

        return salt_and_key
