class Doctor:
    def __init__(self, id, first_name, last_name, specialization, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization
        self.email = email
        self.password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, first_name):
        self.first_name = first_name

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, last_name):
        self.last_name = last_name

    @property
    def specialization(self):
        return self.specialization

    @specialization.setter
    def specialization(self, specialization):
        self.specialization = specialization


    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.email = email

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self._password = password

