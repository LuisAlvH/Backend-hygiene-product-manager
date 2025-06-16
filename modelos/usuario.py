class Usuario:
    def __init__(self, id, nombre, username, password, email ,role):
        self._id = id
        self._nombre = nombre
        self._username = username
        self._password = password
        self._email = email
        self._role= role

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_email(self):
        return self._email
    def get_role(self):
        return self._role

    # Setters
    def set_id(self, id):
        self._id = id

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_email(self, email):
        self._email = email
    def set_rol(self, role):
        self._rol= role
