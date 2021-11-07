from system.models.database.db_handler import UserDB
import hashlib
import os

class Register:
    def __init__(self, user_id: int, user_name: str, password: str, is_admin: bool):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin

    def check_name (self, user_name, user : UserDB):
        if user_name == user.get_user(user_name):
            print("Enter new username")
        else:
            print("Username is available")

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