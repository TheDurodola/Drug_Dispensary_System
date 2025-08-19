class Pharmacist:
    def __init__( self ):
        self.id = ""
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""


    @property
    def id( self ):
        return self.id

    @id.setter
    def id( self, id ):
        self.id = id

    @property
    def first_name( self ):
        return self.first_name

    @first_name.setter
    def first_name( self, first_name ):
        self.first_name = first_name

    @property
    def last_name( self ):
        return self.last_name

    @last_name.setter
    def last_name( self, last_name ):
        self.last_name = last_name


    @property
    def email( self ):
        return self.email

    @email.setter
    def email( self, email ):
        self.email = email

    @property
    def password( self ):
        return self.password

    @password.setter
    def password( self, password ):
        self.password = password
