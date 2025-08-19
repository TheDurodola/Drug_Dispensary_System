class Admin:
    def __init__(self):
        self._username = "admin"
        self._password = "admin"

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
