# user.py
############################
# various classes for the user
#############################
# Author: Wasim - 17193559
# Last edited on 01/11
# Modification time 10:33 AM

import hashlib
import os


class User:
    def __init__(self, user_id: int, user_name: str, password: str, is_admin: bool, country: str):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin
        self._country = country

    def get_user(self):
        return [self._user_id, self._user_name, self._password, self._is_admin, self._country]

    def get_user_id(self):
        return self._user_id

    def get_user_name(self):
        return self._user_name

    def get_password(self):
        return self._password

    def get_is_admin(self):
        return self._is_admin

    def get_country(self):
        return self._country

    def set_user(self):
        print("The username= ", self._user_name, "\tThe password= ",
              self._password, "\tis the user admin= ", self._is_admin)
        self.get_hashed_password(self._password)

    def get_hashed_password(self, password: str) -> str:
        # https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
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


# child class (admin) is push the information to the super class (user)


print(User.get_hashed_password("1234567","123456"))
# this line of code just to test

# x.set_newUser()
