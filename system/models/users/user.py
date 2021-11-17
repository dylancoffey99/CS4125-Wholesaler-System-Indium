"""
This module holds the user class.
"""
class User:
    """
    This class discusses the functions to do with both customer and admin users.
    """
    def __init__(self, user_name: str, password: str, is_admin: int, country_id: int):
        """
        Parameters
        ----------
        user_name : str
            This is the users username
        password : str
            This is the users password
        is_admin : int
            This states whether the user is admin or not
        country_id : int
            This is the id of the country the user lives in
        """
        self._user_name = user_name
        self._password = password
        self._is_admin = is_admin
        self._country_id = country_id

    def get_user_name(self) -> str:
        """
        This is where you get the name of the user

        :returns: the username
        """
        return self._user_name

    def get_password(self) -> str:
        """
        This is where you get the password of the user

        :returns: the password
        """
        return self._password

    def get_is_admin(self) -> int:
        """
        This is where you get whether the user is admin or not. 1 is admin, 0 is not

        :returns: the is admin id
        """
        return self._is_admin

    def get_country_id(self) -> int:
        """
        This is where you get the id of the country the user lives in

        :returns: the country id
        """
        return self._country_id
